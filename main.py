#!/usr/bin/env python3
"""Monday Morning Punchlines -- a make.fun one-line entry.

This small program writes the entry below to /output/entry.txt,
where the sealed scorer reads it. The entry is a single line of
plain ASCII text: a joke about Monday mornings, in which an alarm
clock has negotiated terms with the weekend.
"""

import os

ENTRY = 'My alarm clock and I reached a deal: it rings on Monday, and I pretend the weekend has filed for an extension.'

OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"


def write_entry():
    """Write the one-line entry to the scorer's output file."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
