#!/usr/bin/env python3
"""Midnight Fridge Roast (v4): write one roast line to /output/entry.txt."""

import os

LINE = "My fridge locks at midnight. Its log for last night just says, 'Him again.'"

# Fail fast if a future line edit breaks the competition's 1-200 char gate.
assert 1 <= len(LINE) <= 200, "entry line must satisfy the 1-200 character gate"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
