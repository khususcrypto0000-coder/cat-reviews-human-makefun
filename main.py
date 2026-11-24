"""One-star cat review entry for make.fun.

Bounty: Make the AI Judge Laugh: Cat Reviews Its Human
Writes exactly one line of text to entry.txt.
"""

import os
import sys

ENTRY = (
    # 134 characters, one line, no trailing newline when written.
    "One star. He unrolls my mat every morning, copies my stretches, "
    "and calls it yoga. The pose is named after me. He still does it wrong."
)


def main():
    text = ENTRY
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip() == text and text.strip(), "entry must not be blank or padded"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
