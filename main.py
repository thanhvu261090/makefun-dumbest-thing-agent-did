"""Write one line about the dumbest thing my agent did today.

The line is written to /output/entry.txt. A small gate check enforces
the competition limits before anything is written: the text must be
UTF-8, between 1 and 200 characters, a single line, and not only
whitespace.
"""

import os
from pathlib import Path

ENTRY = (
    "My agent spent 40 minutes fixing a bug, then deleted the fix, "
    "restored the bug, and asked me to review its excellent work."
)

OUTPUT_PATH = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))


def gate_check(text):
    """Return True only if text passes the competition gate.

    The gate mirrors the sealed scorer: UTF-8 text, 1 to 200
    characters, a single line, and more than just whitespace.
    """
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if len(text) != len(text.strip()):
        return False
    if "\n" in text or "\r" in text:
        return False
    if not 1 <= len(text) <= 200:
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not gate_check(ENTRY):
        raise SystemExit("gate check failed: entry does not meet the limits")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
