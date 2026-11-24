#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes one line, the funniest excuse an AI agent could give after
failing a task, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Standard library only: no network, no clock, no randomness, so two
runs produce byte-identical output.
"""

import os
import sys

EXCUSE = (
    "I typed the perfect solution into the wrong window. "
    "Your neighbour's smart fridge now runs your startup, "
    "and it wants a raise."
)


def validate(text: str) -> None:
    """Gate: 1 to 200 characters, not only white space, one line."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"excuse must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("excuse must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")


def main() -> int:
    validate(EXCUSE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="") as fh:
        fh.write(EXCUSE)
    # Read-back verification: refuse to hand the grader a truncated
    # or corrupted file — the bytes on disk must match the excuse.
    with open(target, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != EXCUSE:
        print("entry.txt does not match the excuse after write", file=sys.stderr)
        return 1
    print(f"wrote {target} ({len(EXCUSE)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
