"""
bootstrap.py — Download pre-built data files from the latest GitHub Release.

Fetches rnaseq_classified.json and ftp_index.json so you can skip the full
pipeline (~18 hours) and go straight to querying or rebuilding the wiki.

Usage:
    conda run -n GEO_llm python scripts/bootstrap.py [--include-raw] [--force]

Options:
    --include-raw   Also download raw_data.tar.gz (quarterly GEO metadata snapshots,
                    ~50 MB compressed). Only needed to re-run the pipeline from scratch.
    --force         Overwrite existing files without prompting.
    --release TAG   Use a specific release tag instead of the latest (e.g. data-v1.0.0).

Requires no external dependencies — stdlib only.
"""

import argparse
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

BOOTSTRAP_ASSET = "bootstrap_data.tar.gz"
RAW_ASSET = "raw_data.tar.gz"

# Files extracted from bootstrap_data.tar.gz and where they land
BOOTSTRAP_FILES = ["rnaseq_classified.json", "ftp_index.json"]


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json",
                                               "User-Agent": "GEO_llm-bootstrap/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def get_release(tag: str | None) -> dict:
    if tag:
        url = f"{API_BASE}/repos/{REPO}/releases/tags/{tag}"
        print(f"Fetching release {tag}...")
    else:
        url = f"{API_BASE}/repos/{REPO}/releases/latest"
        print("Fetching latest data release...")
    try:
        return fetch_json(url)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            sys.exit(f"Error: release not found at {url}\n"
                     "Check that a data release exists: "
                     f"https://github.com/{REPO}/releases")
        raise


def find_asset(release: dict, name: str) -> dict | None:
    for asset in release.get("assets", []):
        if asset["name"] == name:
            return asset
    return None


def download_with_progress(url: str, dest: str, label: str) -> None:
    req = urllib.request.Request(url, headers={
        "Accept": "application/octet-stream",
        "User-Agent": "GEO_llm-bootstrap/1.0",
    })
    with urllib.request.urlopen(req, timeout=60) as resp:
        total = int(resp.headers.get("Content-Length", 0))
        downloaded = 0
        chunk = 64 * 1024
        with open(dest, "wb") as f:
            while True:
                buf = resp.read(chunk)
                if not buf:
                    break
                f.write(buf)
                downloaded += len(buf)
                if total:
                    pct = downloaded / total * 100
                    mb = downloaded / 1_048_576
                    total_mb = total / 1_048_576
                    print(f"\r  {label}: {mb:.1f} / {total_mb:.1f} MB ({pct:.0f}%)",
                          end="", flush=True)
    print()  # newline after progress


def confirm_overwrite(paths: list[str], force: bool) -> bool:
    existing = [p for p in paths if os.path.exists(p)]
    if not existing:
        return True
    if force:
        return True
    print("The following files already exist:")
    for p in existing:
        size_mb = os.path.getsize(p) / 1_048_576
        print(f"  {os.path.relpath(p, PROJECT_ROOT)}  ({size_mb:.0f} MB)")
    answer = input("Overwrite? [y/N] ").strip().lower()
    return answer == "y"


def download_and_extract(asset: dict, dest_paths: list[str], label: str) -> None:
    with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        print(f"Downloading {asset['name']} ({asset['size'] / 1_048_576:.1f} MB)...")
        download_with_progress(asset["browser_download_url"], tmp_path, label)

        print(f"Extracting...")
        with tarfile.open(tmp_path, "r:gz") as tf:
            members = tf.getmembers()
            for member in members:
                # Strip any leading path components — extract flat into PROJECT_ROOT
                member.name = os.path.basename(member.name)
                if not member.name:
                    continue
                dest = os.path.join(PROJECT_ROOT, member.name)
                print(f"  -> {member.name}")
                with tf.extractfile(member) as src, open(dest, "wb") as out:
                    out.write(src.read())
    finally:
        os.unlink(tmp_path)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--include-raw", action="store_true",
                        help="Also download raw quarterly GEO metadata snapshots (~50 MB)")
    parser.add_argument("--force", action="store_true",
                        help="Overwrite existing files without prompting")
    parser.add_argument("--release", metavar="TAG",
                        help="Use a specific release tag (default: latest)")
    args = parser.parse_args()

    release = get_release(args.release)
    tag = release["tag_name"]
    published = release["published_at"][:10]
    print(f"Release: {tag}  (published {published})")
    print(f"  {release.get('body', '').splitlines()[0] if release.get('body') else ''}")
    print()

    # --- bootstrap bundle (intermediates) ---
    bootstrap_asset = find_asset(release, BOOTSTRAP_ASSET)
    if not bootstrap_asset:
        sys.exit(f"Error: no '{BOOTSTRAP_ASSET}' asset found in release {tag}.\n"
                 "The release may have been created without data assets.")

    dest_paths = [os.path.join(PROJECT_ROOT, f) for f in BOOTSTRAP_FILES]
    if not confirm_overwrite(dest_paths, args.force):
        print("Skipping bootstrap bundle.")
    else:
        download_and_extract(bootstrap_asset, dest_paths, BOOTSTRAP_ASSET)
        print(f"Bootstrap data ready: {', '.join(BOOTSTRAP_FILES)}")

    # --- raw data bundle (optional) ---
    if args.include_raw:
        raw_asset = find_asset(release, RAW_ASSET)
        if not raw_asset:
            print(f"Warning: no '{RAW_ASSET}' asset found in release {tag} — skipping.")
        else:
            raw_dest = os.path.join(PROJECT_ROOT, "data")
            os.makedirs(raw_dest, exist_ok=True)
            if confirm_overwrite([raw_dest], args.force):
                download_and_extract(raw_asset, [raw_dest], RAW_ASSET)
                print("Raw data ready: data/")

    print("\nDone. You can now run:")
    print("  conda run -n GEO_llm python scripts/build_search_index.py")
    print("  conda run -n GEO_llm python scripts/generate_wiki.py")


if __name__ == "__main__":
    main()
