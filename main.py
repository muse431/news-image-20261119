#!/usr/bin/env python3
"""make.fun entry: news-image-20261119 - "Sum up 19 November's world news in one image".

The finished poster ships in this repository as ``poster.png`` (a newspaper
front page for Thursday 19 November 2026). This program copies those bytes to
the required output location, so every run produces an identical file.
Standard library only; runs offline in well under a second.
"""

import os
from pathlib import Path

ASSET_NAME = "poster.png"
OUTPUT_NAME = "entry.png"
FALLBACK_OUTPUT_DIR = "/output"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def main() -> None:
    here = Path(__file__).resolve().parent
    asset = here / ASSET_NAME
    if not asset.is_file():
        raise SystemExit(f"asset not found: {asset}")

    # Read the poster once and sanity-check it before publishing: the bytes
    # must be a real PNG, so a truncated or swapped asset fails loudly here
    # instead of reaching the judge as a broken image.
    data = asset.read_bytes()
    if not data.startswith(PNG_SIGNATURE):
        raise SystemExit(f"asset is not a PNG file: {asset}")

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or FALLBACK_OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)

    destination = output_dir / OUTPUT_NAME
    destination.write_bytes(data)
    if destination.stat().st_size != len(data):
        raise SystemExit(f"output size mismatch for {destination}")
    print(f"wrote {destination} ({len(data)} bytes)")


if __name__ == "__main__":
    main()
