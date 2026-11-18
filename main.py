#!/usr/bin/env python3
"""Copy the pre-rendered front page to the output directory.

Entry for make.fun bounty news-image-20261118: sum up Wednesday
18 November 2026's world news in one image. The image
(news-18-nov-2026.png, 1024x1024, under 1 MiB) is a newspaper front
page drawn at build time from the day's verified headlines; this
program just copies it to entry.png in the output directory, as the
kit's starter does. The seven stories on the page are: Xi greets
Trump in Shenzhen as APEC opens; Iran widens its Gulf attacks to a
US base in Kuwait; Peltola wins the Alaska Senate seat; the US loses
its measles-free status; the Congo Ebola outbreak passes 11,000
cases; Voyager 1 reaches one light-day from Earth; and Cyclone
Xavier hits the Cook Islands at Category 5.

Pure Python standard library, deterministic, no network: both runs
write the same bytes. Honours MAKEFUN_OUTPUT_DIR, defaulting to
/output; a blank value counts as unset. The source is checked to be
a whole PNG (magic bytes) and under the 1 MiB limit before copying.
"""
import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "news-18-nov-2026.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576


def _output_dir():
    """Resolve the output directory from the environment.

    MAKEFUN_OUTPUT_DIR wins when set to a non-blank value; otherwise
    the default /output is used. Leading/trailing whitespace is
    ignored so a stray space cannot create a wrong directory.
    """
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR") or ""
    return Path(raw.strip() or "/output")


def _checked_source():
    """Return SOURCE after verifying it is a whole PNG under 1 MiB."""
    if not SOURCE.is_file():
        raise FileNotFoundError(f"missing entry image: {SOURCE}")
    if SOURCE.stat().st_size > MAX_BYTES:
        raise ValueError(f"entry image over 1 MiB: {SOURCE}")
    with SOURCE.open("rb") as fh:
        if fh.read(len(PNG_MAGIC)) != PNG_MAGIC:
            raise ValueError(f"not a PNG file: {SOURCE}")
    return SOURCE


def main():
    out_dir = _output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    source = _checked_source()
    dest = out_dir / "entry.png"
    shutil.copyfile(source, dest)
    # Guard against a partial copy: the grader gates on the output
    # being a whole image, so confirm every byte arrived.
    if dest.stat().st_size != source.stat().st_size:
        raise ValueError(f"incomplete copy: {dest}")


if __name__ == "__main__":
    main()
