#!/usr/bin/env python3
"""Monday Morning Punchlines (make.fun).

Writes the one-line entry to /output/entry.txt, where the sealed
scorer reads it.
"""

import os

ENTRY = 'My alarm clock and I reached a deal: it rings on Monday, and I pretend the weekend has filed for an extension.'


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
