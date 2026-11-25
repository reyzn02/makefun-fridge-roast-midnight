#!/usr/bin/env python3
"""Midnight Fridge Roast (v4): write one roast line to /output/entry.txt."""

import os

LINE = "My fridge locks at midnight. Its log for last night just says, 'Him again.'"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
