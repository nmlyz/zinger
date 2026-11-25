#!/usr/bin/env python3
"""Write one funny line to a text file."""

import os

LINE = (
    'My phone autocorrected "I love you" to "I love yule" in July, '
    "and my girlfriend now thinks I am a seasonal employee."
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
OUTPUT_FILE = "entry.txt"


def main():
    # The directory itself is left alone; only the file gets its mode set.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
