"""
Index GEO FTP supplementary directories for all classified datasets
(RNA-seq + ChIP-seq/ATAC-seq and any other classified assay types).
Extracts actual filenames, sizes, and file counts.

Saves results incrementally to ftp_index.json so it can be resumed if interrupted.
FTP connections are reused and rate-limited to stay within NCBI guidelines.
"""
import ftplib
import json
import os
import sys
import time
from datetime import datetime

FTP_HOST = "ftp.ncbi.nlm.nih.gov"
FTP_INDEX_PATH = "ftp_index.json"
REQUEST_DELAY = 0.35  # seconds between FTP requests
RECONNECT_EVERY = 500  # reconnect FTP after N requests to avoid stale connections
SAVE_EVERY = 100  # save progress every N records


def get_suppl_path(accession):
    """Build the FTP path for a GSE supplementary directory."""
    prefix = accession[:-3] + "nnn" if len(accession) > 6 else "GSEnnn"
    return f"/geo/series/{prefix}/{accession}/suppl/"


def list_ftp_dir(ftp, path):
    """List files in an FTP directory with sizes. Returns list of dicts."""
    files = []
    try:
        entries = []
        ftp.retrlines(f"LIST {path}", entries.append)
        for entry in entries:
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
    except ftplib.error_perm:
        # Directory doesn't exist or no permission
        return []
    except (ftplib.error_temp, EOFError, OSError):
        # Transient error — caller should retry after reconnect
        return None
    return files


def connect_ftp(retries=5, delay=10):
    """Create a new anonymous FTP connection with retry logic."""
    for attempt in range(retries):
        try:
            ftp = ftplib.FTP(FTP_HOST, timeout=30)
            ftp.login()
            return ftp
        except Exception as e:
            if attempt < retries - 1:
                wait = delay * (attempt + 1)
                print(f"  FTP connect failed ({e}), retrying in {wait}s... "
                      f"(attempt {attempt + 2}/{retries})")
                time.sleep(wait)
            else:
                raise


def load_existing_index():
    """Load previously saved index, or return empty dict."""
    if os.path.exists(FTP_INDEX_PATH):
        with open(FTP_INDEX_PATH) as f:
            return json.load(f)
    return {}


def save_index(index):
    """Save index to disk."""
    with open(FTP_INDEX_PATH, "w") as f:
        json.dump(index, f, indent=2)


def main():
    # Load all classified records (RNA-seq + any other assay types)
    accessions_seen: set[str] = set()
    accessions: list[str] = []

    for classified_file in ("rnaseq_classified.json", "chipseq_classified.json", "methylation_classified.json"):
        if os.path.exists(classified_file):
            with open(classified_file) as f:
                records = json.load(f)
            new = [r["accession"] for r in records
                   if r["accession"] and r["accession"] not in accessions_seen]
            accessions.extend(new)
            accessions_seen.update(new)
            print(f"Loaded {len(new):,} accessions from {classified_file}")
        else:
            print(f"Skipping {classified_file} (not found)")

    print(f"Total unique accessions to index: {len(accessions):,}")

    # Load existing progress
    index = load_existing_index()
    already_done = set(index.keys())
    todo = [a for a in accessions if a not in already_done]
    print(f"Already indexed: {len(already_done)}")
    print(f"Remaining: {len(todo)}")

    if not todo:
        print("All done!")
        return

    # Connect
    print(f"\nConnecting to {FTP_HOST}...")
    ftp = connect_ftp()
    print("Connected. Starting indexing...\n")

    completed = 0
    errors = 0
    start_time = time.time()

    try:
        for i, acc in enumerate(todo):
            # Reconnect periodically
            if i > 0 and i % RECONNECT_EVERY == 0:
                try:
                    ftp.quit()
                except Exception:
                    pass
                print(f"  Reconnecting FTP...")
                ftp = connect_ftp()

            path = get_suppl_path(acc)
            files = list_ftp_dir(ftp, path)

            # Retry once on transient error
            if files is None:
                time.sleep(2)
                try:
                    ftp.quit()
                except Exception:
                    pass
                ftp = connect_ftp()
                files = list_ftp_dir(ftp, path)
                if files is None:
                    files = []
                    errors += 1

            # Store result
            total_size = sum(f["size"] for f in files)
            index[acc] = {
                "files": [{"name": f["name"], "size": f["size"]} for f in files if not f["is_dir"]],
                "n_files": len([f for f in files if not f["is_dir"]]),
                "total_size": total_size,
                "indexed_at": datetime.now().isoformat(),
            }
            completed += 1

            # Progress
            if completed % 50 == 0:
                elapsed = time.time() - start_time
                rate = completed / elapsed
                remaining = (len(todo) - completed) / rate if rate > 0 else 0
                print(f"  {completed}/{len(todo)} indexed "
                      f"({rate:.1f}/sec, ~{remaining/60:.0f}min remaining, {errors} errors)")

            # Save periodically
            if completed % SAVE_EVERY == 0:
                save_index(index)

            time.sleep(REQUEST_DELAY)
    except (KeyboardInterrupt, Exception) as e:
        print(f"\n  Interrupted ({e}). Saving progress...")
        save_index(index)
        print(f"  Saved {len(index)} records to {FTP_INDEX_PATH}")
        raise

    # Final save
    save_index(index)

    try:
        ftp.quit()
    except Exception:
        pass

    elapsed = time.time() - start_time
    print(f"\nDone! Indexed {completed} accessions in {elapsed/60:.1f} min")
    print(f"Errors: {errors}")
    print(f"Total indexed: {len(index)}")

    # Quick stats
    sizes = [v["total_size"] for v in index.values()]
    file_counts = [v["n_files"] for v in index.values()]
    print(f"\nFile count distribution:")
    print(f"  0 files: {sum(1 for c in file_counts if c == 0)}")
    print(f"  1 file:  {sum(1 for c in file_counts if c == 1)}")
    print(f"  2-5:     {sum(1 for c in file_counts if 2 <= c <= 5)}")
    print(f"  6-20:    {sum(1 for c in file_counts if 6 <= c <= 20)}")
    print(f"  21+:     {sum(1 for c in file_counts if c > 20)}")


if __name__ == "__main__":
    main()
