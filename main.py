#!/usr/bin/env python3
"""Print the one-line entry from entry.txt (cwd-independent)."""
import os
import sys


def main():
    # Resolve via __file__: the grader runs main.py from an arbitrary cwd
    # on a read-only FS, so a relative "entry.txt" would not be found.
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
