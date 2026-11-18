#!/usr/bin/env python3
"""news-image-20261118 entry (Python 3.13, standard library only).

Writes one image summing up the world's news of Wednesday 18 November 2026
to /output/entry.png. The image is the entry.png beside this file: a
newspaper front page drawn for the day's news (Trump-Xi-Putin summit in
Shenzhen; the U.S.-Iran strikes in the Gulf; Ukraine's second-day strike on
the Crimea Bridge; the Democrats' Alaska Senate win; the Ebola outbreak in
DR Congo; and the Siberian plane crash), and this program copies it to the
output directory byte for byte.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

SRC = HERE / "entry.png"
with SRC.open("rb") as f:
    if f.read(len(PNG_SIGNATURE)) != PNG_SIGNATURE:
        raise SystemExit(f"entry image is not a valid PNG: {SRC}")

OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, OUT_DIR / "entry.png")
