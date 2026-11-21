#!/usr/bin/env python3
"""Copy the travel poster to the output directory.

Entry program for the-poster-for-a-place-that-i-2-20261121-0539.
Standard library only: the poster image ships in this repo as entry.png,
and this program copies it to $MAKEFUN_OUTPUT_DIR/entry.png.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
MAX_BYTES = 1_048_576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(SRC, "rb") as f:
        head = f.read(8)
    if head != PNG_MAGIC:
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    size = os.path.getsize(SRC)
    if size > MAX_BYTES:
        print(f"entry.png is {size} bytes, over the 1 MiB limit", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    with open(dst, "rb") as f:
        copied = f.read()
    with open(SRC, "rb") as f:
        original = f.read()
    if copied != original:
        print("copied entry.png does not match the source", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
