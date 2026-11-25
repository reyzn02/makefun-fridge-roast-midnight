#!/usr/bin/env python3
"""Midnight Fridge Roast: one line roasting a smart fridge that
refuses to open after midnight.

The program writes a single line, 1-200 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python standard library only, no network calls, deterministic output.
"""

import os

LINE = (
    "My fridge has a midnight curfew: one beep, the door locks, "
    "and the screen says, 'You've had enough, champ.'"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        raise SystemExit("entry line fails the 1-200 character gate")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
