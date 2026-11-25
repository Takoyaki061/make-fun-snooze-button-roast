#!/usr/bin/env python3
"""Snooze Button Roast — writes one roast line to /output/entry.txt.

Entry for make.fun's "Snooze Button Roast" bounty: one line roasting an
alarm clock that rings at 6 AM on a Saturday morning.

The gate requires /output/entry.txt to hold UTF-8 text of 1 to 200
characters, not only whitespace, so the program checks that itself
before it writes: a line that breaks the gate fails loudly here
instead of silently submitting an invalid entry.
"""

import os

ROAST = (
    "My alarm is that colleague who schedules a 6 AM \"quick sync\" "
    "on Saturday and cc's the entire weekend just to watch it burn."
)


def main():
    if not 1 <= len(ROAST) <= 200 or not ROAST.strip():
        raise SystemExit("roast must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
