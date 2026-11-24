#!/usr/bin/env python3
"""Fortune in a Pot — make.fun entry.

Writes one fortune for a houseplant (<=120 chars) to /output/entry.txt.
Chosen line: a ladybug lands on the tallest leaf and declares it the best
seat in the house. Field research (207 submissions, 24 Nov 2026): the ladybug
angle is 0-hit in the field; the dominant cliches (outgrow-the-pot, new leaf,
sunbeam, cat, keeper-bragging) are all avoided.
"""

import os

ENTRY = "A ladybug will land on your tallest leaf this week and declare it the best seat in the house."


MAX_CHARS = 120


def validate_entry(text):
    """Brief-format guard: one line, 1-120 chars, no leading/trailing space."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if text != text.strip() or "\n" in text:
        raise ValueError("entry must be a single line without surrounding space")
    return text


def main():
    validate_entry(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise ValueError("read-back mismatch: file content != ENTRY")


if __name__ == "__main__":
    main()
