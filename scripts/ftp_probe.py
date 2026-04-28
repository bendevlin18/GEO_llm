"""
Probe GEO FTP supplementary directories to get actual file listings.
Tests a few datasets to understand the FTP structure and what info we can extract.
"""
import ftplib
import json
import time

FTP_HOST = "ftp.ncbi.nlm.nih.gov"

# Sample accessions across modalities
TEST_ACCESSIONS = [
    "GSE313444",   # scRNA-seq, reported "MTX, TSV"
    "GSE283790",   # bulk, reported "CSV"
    "GSE291610",   # snRNA-seq, reported "H5AD"
    "GSE318565",   # spatial, reported "CSV, H5"
    "GSE326276",   # bulk, reported "RDS"
    "GSE307181",   # bulk, reported "TXT"
]


def get_suppl_path(accession):
    """Build the FTP path for a GSE supplementary directory."""
    prefix = accession[:-3] + "nnn" if len(accession) > 6 else "GSEnnn"
    return f"/geo/series/{prefix}/{accession}/suppl/"


def list_ftp_dir(ftp, path):
    """List files in an FTP directory with sizes."""
    files = []
    try:
        entries = []
        ftp.retrlines(f"LIST {path}", entries.append)
        for entry in entries:
            # Parse FTP LIST output: permissions, links, owner, group, size, date, name
            parts = entry.split(None, 8)
            if len(parts) >= 9:
                size = int(parts[4])
                name = parts[8]
                is_dir = entry.startswith("d")
                files.append({
                    "name": name,
                    "size": size,
                    "is_dir": is_dir,
                })
    except ftplib.error_perm as e:
        print(f"  Error listing {path}: {e}")
    return files


def format_size(size_bytes):
    """Human-readable file size."""
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"


def main():
    print(f"Connecting to {FTP_HOST}...")
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login()  # anonymous
    print("Connected.\n")

    results = {}
    for acc in TEST_ACCESSIONS:
        path = get_suppl_path(acc)
        print(f"--- {acc} ---")
        print(f"  Path: {path}")

        files = list_ftp_dir(ftp, path)
        results[acc] = files

        if files:
            total_size = sum(f["size"] for f in files)
            print(f"  {len(files)} files, total {format_size(total_size)}")
            for f in files:
                print(f"    {format_size(f['size']):>10}  {f['name']}")
        else:
            print("  No files found or directory doesn't exist")

        print()
        time.sleep(0.5)

    ftp.quit()

    # Save results
    with open("ftp_probe_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("Saved to ftp_probe_results.json")


if __name__ == "__main__":
    main()
