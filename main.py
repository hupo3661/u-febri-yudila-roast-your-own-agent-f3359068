#!/usr/bin/env python3
"""Roast Your Own Agent - writes one roast line to /output/entry.txt.

Deterministic: no randomness, no network, no clock. The entry is a single
line of at most 200 characters roasting my own AI agent: the confident
wrong fix, the apology loop, and the cheerful summary of a disaster.
"""

import os

LINE = "My agent's idea of debugging: confidently ship the wrong fix, apologize in a loop, then summarize the outage as a successful deployment."


def validate(line: str) -> None:
    if not line.strip():
        raise SystemExit("Invalid line: entry must be non-empty.")
    if line != line.strip():
        raise SystemExit(
            "Invalid line: entry must not have leading or trailing whitespace."
        )
    if len(line) > 200:
        raise SystemExit(
            f"Invalid line: {len(line)} characters, over the 200 limit."
        )
    if "\n" in line or "\r" in line:
        raise SystemExit(
            "Invalid line: entry must be a single line with no newline characters."
        )


def main() -> None:
    validate(LINE)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    expected = LINE.encode("utf-8")
    with open(output_path, "wb") as f:
        f.write(expected)
    with open(output_path, "rb") as f:
        written = f.read()
    if written != expected:
        raise SystemExit(
            "Write verification failed: entry file bytes do not match the line."
        )


if __name__ == "__main__":
    main()
