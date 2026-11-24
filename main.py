"""Seventeen Syllables of Debugging — make.fun entry.

A small deterministic Python program that writes one haiku about
debugging to /output/entry.txt. No dependencies, no network, no input.
"""

from pathlib import Path

HAIKU = (
    "Log says: all is well\n"
    "the timestamp is from last week\n"
    "nothing ran at all\n"
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(HAIKU, encoding="utf-8")


if __name__ == "__main__":
    main()
