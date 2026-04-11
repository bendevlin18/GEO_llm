"""
create_data_release.py — Create a GitHub Release and upload data assets.

Admin/maintainer script. Run this whenever you want to publish a new data snapshot
for others to bootstrap from.

Usage:
    GITHUB_TOKEN=ghp_... conda run -n GEO_llm python scripts/create_data_release.py \
        --tag data-v1.0.0 \
        [--include-raw] \
        [--notes "Coverage: 2015-Q1 through April 2026, 130k RNA-seq datasets"]

Options:
    --tag TAG         Release tag to create (e.g. data-v1.0.0). Required.
    --include-raw     Also package and upload data/ as raw_data.tar.gz (~50 MB compressed).
    --notes TEXT      Release body text (summary of data coverage).
    --draft           Create as a draft release (don't publish immediately).

Requires:
    - GITHUB_TOKEN env var with repo write access
    - rnaseq_classified.json and ftp_index.json to exist in the project root
    - data/ directory to exist (only if --include-raw)

Stdlib only — no external dependencies.
"""

import argparse
import gzip
import json
import os
import sys
import tarfile
import tempfile
import urllib.error
import urllib.request

REPO = "bendevlin18/GEO_llm"
API_BASE = "https://api.github.com"
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BOOTSTRAP_FILES = [
    ("rnaseq_classified.json", "rnaseq_classified.json"),
    ("ftp_index.json", "ftp_index.json"),
]


def get_token() -> str:
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if not token:
        sys.exit("Error: GITHUB_TOKEN environment variable not set.\n"
                 "Create a token at https://github.com/settings/tokens with 'repo' scope.")
    return token


def api_request(method: str, path: str, token: str, data: bytes | None = None,
                content_type: str = "application/json") -> dict:
    url = f"{API_BASE}{path}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "GEO_llm-release/1.0",
        "Content-Type": content_type,
    }
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        sys.exit(f"GitHub API error {e.code} for {method} {url}:\n{body}")


def upload_asset(upload_url: str, token: str, path: str, name: str) -> None:
    # upload_url from the release object looks like:
    # https://uploads.github.com/repos/.../releases/123/assets{?name,label}
    base_url = upload_url.split("{")[0]
    url = f"{base_url}?name={name}"

    size = os.path.getsize(path)
    print(f"  Uploading {name} ({size / 1_048_576:.1f} MB)...")

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "GEO_llm-release/1.0",
        "Content-Type": "application/gzip",
        "Content-Length": str(size),
    }

    with open(path, "rb") as f:
        req = urllib.request.Request(url, data=f.read(), headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            result = json.loads(resp.read())
            print(f"  -> {result['browser_download_url']}")
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        sys.exit(f"Upload failed {e.code}:\n{body}")


def make_tarball(out_path: str, sources: list[tuple[str, str]]) -> None:
    """Create a .tar.gz from a list of (src_path, archive_name) tuples."""
    with tarfile.open(out_path, "w:gz", compresslevel=6) as tf:
        for src, arcname in sources:
            size_mb = os.path.getsize(src) / 1_048_576
            print(f"  Adding {arcname} ({size_mb:.0f} MB)...")
            tf.add(src, arcname=arcname)


def make_raw_tarball(out_path: str, data_dir: str) -> None:
    """Package all quarterly JSON files from data/ into a tarball."""
    with tarfile.open(out_path, "w:gz", compresslevel=6) as tf:
        for fname in sorted(os.listdir(data_dir)):
            if not fname.endswith(".json"):
                continue
            src = os.path.join(data_dir, fname)
            size_mb = os.path.getsize(src) / 1_048_576
            print(f"  Adding data/{fname} ({size_mb:.0f} MB)...")
            tf.add(src, arcname=f"data/{fname}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--tag", required=True,
                        help="Release tag (e.g. data-v1.0.0)")
    parser.add_argument("--include-raw", action="store_true",
                        help="Also upload raw_data.tar.gz (data/ quarterly snapshots)")
    parser.add_argument("--notes", default="",
                        help="Release body / description")
    parser.add_argument("--draft", action="store_true",
                        help="Create as draft release")
    args = parser.parse_args()

    token = get_token()

    # Verify source files exist
    missing = []
    for _, local_name in BOOTSTRAP_FILES:
        path = os.path.join(PROJECT_ROOT, local_name)
        if not os.path.exists(path):
            missing.append(local_name)
    if missing:
        sys.exit(f"Error: missing required files: {', '.join(missing)}\n"
                 "Run the pipeline first or restore from a previous run.")

    if args.include_raw:
        data_dir = os.path.join(PROJECT_ROOT, "data")
        if not os.path.isdir(data_dir) or not any(f.endswith(".json") for f in os.listdir(data_dir)):
            sys.exit("Error: data/ directory is empty or missing. "
                     "Cannot create raw data bundle.")

    with tempfile.TemporaryDirectory() as tmp:
        # --- Create bootstrap bundle ---
        bootstrap_path = os.path.join(tmp, "bootstrap_data.tar.gz")
        print("Creating bootstrap_data.tar.gz...")
        sources = [(os.path.join(PROJECT_ROOT, local), local)
                   for _, local in BOOTSTRAP_FILES]
        make_tarball(bootstrap_path, sources)
        size_mb = os.path.getsize(bootstrap_path) / 1_048_576
        print(f"  bootstrap_data.tar.gz: {size_mb:.1f} MB compressed\n")

        # --- Create raw bundle (optional) ---
        raw_path = None
        if args.include_raw:
            raw_path = os.path.join(tmp, "raw_data.tar.gz")
            print("Creating raw_data.tar.gz...")
            make_raw_tarball(raw_path, os.path.join(PROJECT_ROOT, "data"))
            size_mb = os.path.getsize(raw_path) / 1_048_576
            print(f"  raw_data.tar.gz: {size_mb:.1f} MB compressed\n")

        # --- Create GitHub release ---
        print(f"Creating GitHub release {args.tag}...")
        body = args.notes or (
            f"Data snapshot for GEO RNA-seq wiki.\n\n"
            f"**bootstrap_data.tar.gz** — `rnaseq_classified.json` + `ftp_index.json` "
            f"(skip the full pipeline, ~18 hrs)\n\n"
            f"To use:\n"
            f"```bash\n"
            f"conda run -n GEO_llm python scripts/bootstrap.py\n"
            f"```"
        )
        payload = json.dumps({
            "tag_name": args.tag,
            "name": args.tag,
            "body": body,
            "draft": args.draft,
            "prerelease": False,
        }).encode()

        release = api_request("POST", f"/repos/{REPO}/releases", token, data=payload)
        release_id = release["id"]
        release_url = release["html_url"]
        upload_url = release["upload_url"]
        print(f"  Release created: {release_url}\n")

        # --- Upload assets ---
        print("Uploading assets...")
        upload_asset(upload_url, token, bootstrap_path, "bootstrap_data.tar.gz")
        if raw_path:
            upload_asset(upload_url, token, raw_path, "raw_data.tar.gz")

    print(f"\nDone! Release published at:\n  {release_url}")


if __name__ == "__main__":
    main()
