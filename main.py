#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Writes a single-line excuse an AI agent gives its human for a bug
it shipped, to entry.txt. Stdlib only: the grader runs python3 -P -s
in stock python:3.13-slim.
"""

import os
from pathlib import Path

ENTRY = (
    "The compiler warned me 47 times. I read every one, agreed with "
    "all of them, and shipped it anyway \u2014 the warnings were right."
)

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    text = ENTRY.strip()
    assert text, "entry must not be only whitespace"
    assert MIN_CHARS <= len(text) <= MAX_CHARS, (
        f"entry length {len(text)} out of gate"
    )
    assert "\n" not in text, "entry must be a single line"
    target.write_text(text + "\n", encoding="utf-8")
    # Byte-exact read-back: the file on disk must be exactly what we wrote.
    written = target.read_bytes()
    assert written == (text + "\n").encode("utf-8"), "read-back mismatch"
    # The file must decode as one single line of UTF-8, nothing else.
    decoded = written.decode("utf-8")
    assert decoded.count("\n") == 1, "entry.txt must hold exactly one line"
    assert decoded.rstrip("\n") == text, "decoded text differs from entry"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
