#!/usr/bin/env python3

"""
Recursively scans the current working directory for PDF files,
writes each PDF's full path as a separate line into pdfs_paths.csv.

Behavior:
- Search starts from the directory where the program is executed (Path.cwd()).
- Matches files with extension .pdf (case-insensitive).
- Creates/overwrites pdfs_paths.csv in the same working directory.
- Prints basic error messages in case of failure.
"""

import sys
import csv
from pathlib import Path

def find_pdfs(root: Path):
    results = []
    try:
        for p in root.rglob("*"):
            try:
                if p.is_file() and p.suffix.lower() == ".pdf":
                    results.append(p.resolve())
            except Exception:
                # Skip problematic entries (permission errors, broken symlinks, etc.)
                continue
    except Exception as e:
        raise RuntimeError(f"Failed to traverse {root}: {e}")
    return results

def save_csv(csv_path: Path, paths):
    # Ensure the parent directory exists
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    # Use UTF-8 with BOM so Excel on Windows recognizes UTF-8 automatically
    with csv_path.open(mode="w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        for p in paths:
            writer.writerow([str(p)])

def main():
    root = Path.cwd()

    try:
        pdfs = find_pdfs(root)
    except Exception as e:
        print(f"Error during search: {e}")
        sys.exit(1)

    csv_path = root / "pdfs_paths.csv"
    try:
        save_csv(csv_path, pdfs)
    except Exception as e:
        print(f"Failed to write CSV '{csv_path}': {e}")
        sys.exit(2)

if __name__ == "__main__":
    main()
