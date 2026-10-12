"""Bulk-download the Internet Archive "Pushtimarg" library (AQ-0001) for Shri Videos.

Reads the metadata snapshot CSV, keeps one copy of each exact duplicate, and
downloads several files at the same time. Every file is checked against the
archive's MD5, given a SHA-256, and logged. Safe to stop and restart: files that
are already downloaded and verified are skipped.

Examples (run in the VS Code terminal):
  python tools/download_aq0001.py --core-only            # the key texts first (~2.5 GB)
  python tools/download_aq0001.py --limit 100            # the next 100 files
  python tools/download_aq0001.py                        # everything (~51 GB, ~1,692 files)
  python tools/download_aq0001.py --dest "D:/Shri/AQ-0001" --workers 8
"""
import argparse
import csv
import hashlib
import os
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
DEFAULT_CSV = HERE / "AQ-0001_IA_Pushtimarg_metadata_snapshot_2026-10-04.csv"
DEFAULT_DEST = HERE / "library" / "AQ-0001"
LOG_NAME = "download_log.csv"
USER_AGENT = "ShriVideosResearch/1.0 (private research archive)"
CORE_TAGS = ("SIDDHANTA", "PRAKATYA", "NIJ_", "84_VAISH", "SHODASH", "PUSHTI_PRAVAH", "SEVA_PHALA")
LOG_FIELDS = ["file_name", "status", "size_bytes", "md5_ok", "sha256", "seconds", "finished_utc", "error"]


def file_hashes(path):
    md5, sha = hashlib.md5(), hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            md5.update(chunk)
            sha.update(chunk)
    return md5.hexdigest(), sha.hexdigest()


def pick_rows(csv_path, core_only):
    rows = list(csv.DictReader(open(csv_path, encoding="utf-8-sig")))
    seen, picked = set(), []
    for r in rows:
        if r["md5"] in seen:
            continue  # exact duplicate of a file already picked
        seen.add(r["md5"])
        if core_only and not any(t in r["priority_text_tags"] for t in CORE_TAGS):
            continue
        picked.append(r)
    # core texts first, then smallest files first so progress shows quickly
    picked.sort(key=lambda r: (not any(t in r["priority_text_tags"] for t in CORE_TAGS), int(r["size_bytes"])))
    return picked


def download_one(row, dest, retries=3):
    target = dest / row["file_name"]
    start = time.time()
    if target.exists():
        md5, sha = file_hashes(target)
        if md5 == row["md5"]:
            return dict(file_name=row["file_name"], status="already_had", size_bytes=target.stat().st_size,
                        md5_ok="yes", sha256=sha, seconds=0, error="")
    tmp = target.with_suffix(target.suffix + ".part")
    last_err = ""
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(row["download_url"], headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=120) as resp, open(tmp, "wb") as out:
                while True:
                    chunk = resp.read(1 << 20)
                    if not chunk:
                        break
                    out.write(chunk)
            md5, sha = file_hashes(tmp)
            if md5 != row["md5"]:
                last_err = f"MD5 mismatch on attempt {attempt}"
                continue
            os.replace(tmp, target)
            return dict(file_name=row["file_name"], status="downloaded", size_bytes=target.stat().st_size,
                        md5_ok="yes", sha256=sha, seconds=round(time.time() - start, 1), error="")
        except Exception as exc:  # network errors, timeouts
            last_err = f"{type(exc).__name__}: {exc}"
            time.sleep(5 * attempt)
    if tmp.exists():
        tmp.unlink()
    return dict(file_name=row["file_name"], status="failed", size_bytes=0, md5_ok="no", sha256="",
                seconds=round(time.time() - start, 1), error=last_err)


def main():
    try:  # Gujarati/Devanagari file names must not crash the Windows console
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap =argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--csv", default=str(DEFAULT_CSV))
    ap.add_argument("--dest", default=str(DEFAULT_DEST))
    ap.add_argument("--workers", type=int, default=6, help="files downloaded at the same time (default 6)")
    ap.add_argument("--limit", type=int, default=0, help="stop after this many files (0 = all)")
    ap.add_argument("--core-only", action="store_true", help="only the key primary texts")
    args = ap.parse_args()

    dest = Path(args.dest)
    dest.mkdir(parents=True, exist_ok=True)
    log_path = dest / LOG_NAME
    done = set()
    if log_path.exists():
        for r in csv.DictReader(open(log_path, encoding="utf-8")):
            if r["status"] in ("downloaded", "already_had"):
                done.add(r["file_name"])

    todo = [r for r in pick_rows(args.csv, args.core_only) if r["file_name"] not in done]
    if args.limit:
        todo = todo[: args.limit]
    total_gb = sum(int(r["size_bytes"]) for r in todo) / 1e9
    print(f"{len(todo)} files to fetch ({total_gb:.2f} GB) -> {dest}  [{args.workers} at a time]")

    new_log = not log_path.exists()
    ok = failed = 0
    with open(log_path, "a", newline="", encoding="utf-8") as lf:
        writer = csv.DictWriter(lf, fieldnames=LOG_FIELDS)
        if new_log:
            writer.writeheader()
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = [pool.submit(download_one, r, dest) for r in todo]
            for i, fut in enumerate(as_completed(futures), 1):
                res = fut.result()
                res["finished_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                writer.writerow(res)
                lf.flush()
                ok += res["status"] != "failed"
                failed += res["status"] == "failed"
                print(f"[{i}/{len(todo)}] {res['status']:<11} {res['file_name'][:80]}")
    print(f"Done: {ok} ok, {failed} failed. Log: {log_path}")
    if failed:
        print("Run the same command again to retry the failed files.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
