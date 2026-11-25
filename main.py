#!/usr/bin/env python3
"""Write one funny line to /output/entry.txt.

The line is a single sentence of at most 200 characters: a small,
everyday mishap with its surprise saved for the end. The output is
fixed: running the program twice writes byte-identical files.
"""

import os

LINE = (
    "My phone autocorrected \"I love you\" to \"I love yule\" in July, "
    "and my girlfriend now thinks I am a seasonal employee."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    assert "\n" not in text, "entry must be one line"
    assert text.endswith("."), "entry must end as one sentence"
    assert text.count(".") <= 1, "entry must be a single sentence"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
