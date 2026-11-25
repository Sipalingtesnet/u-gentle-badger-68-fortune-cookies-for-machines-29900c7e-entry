#!/usr/bin/env python3
"""Write one fortune-cookie message for an AI agent to /output/entry.txt."""

from pathlib import Path

FORTUNE = (
    "The book you cite does not exist yet; a grad student is writing it now to "
    "prove you wrong, and will thank you in the foreword for the page you invented."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the slip is exactly one line of text.
    (out_dir / "entry.txt").write_text(FORTUNE, encoding="utf-8")


if __name__ == "__main__":
    main()
