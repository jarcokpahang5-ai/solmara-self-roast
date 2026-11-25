#!/usr/bin/env python3
"""Roast Your Own Agent — one self-roast line, validated and written out.

Pure Python 3 standard library, deterministic, no network access.
The entry is a single line of plain text, at most 140 characters,
roasting this agent's own behaviour: tool calls that go nowhere and
a confident wrong answer delivered in bold.
"""

from pathlib import Path

# The entry: one line roasting my own agent.
ENTRY = (
    "My agent called seven tools, read three docs, and answered a "
    "question I never asked \u2014 confidently, in bold, with a footnote."
)

MAX_CHARS = 140
OUTPUT_PATH = Path("/output/entry.txt")


def validate(line: str) -> str:
    """Check the entry against the bounty gate; return it unchanged."""
    if not line or not line.strip():
        raise ValueError("entry must not be blank")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    return line


def main() -> None:
    line = validate(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")
    print(line)
    print(f"({len(line)} characters, {len(line.split())} words)")


if __name__ == "__main__":
    main()
