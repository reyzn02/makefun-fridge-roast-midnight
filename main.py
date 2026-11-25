#!/usr/bin/env python3
"""Midnight Fridge Roast (v3) — writes one roast line to entry.txt.

The line is a one-line roast of a smart fridge that refuses to open
after midnight. Gate: UTF-8 text of 1 to 200 characters, not only
whitespace. Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output).
"""

import os
import sys

LINE = "My fridge won't open after midnight. It just hums, 'You've already eaten today. I was there.'"


def main() -> int:
    if not LINE or len(LINE) > 200:
        print(f"entry must be 1-200 chars, got {len(LINE)}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
