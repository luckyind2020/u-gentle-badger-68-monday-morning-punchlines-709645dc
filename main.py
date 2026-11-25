"""Monday Morning Punchlines — entry runner.

Loads the single Monday-morning joke stored in output/entry.txt
and prints it. The joke itself lives in the text file; this module
only handles locating it, trimming stray whitespace, and refusing
to print an empty entry.
"""

from pathlib import Path

ENTRY_PATH = Path(__file__).resolve().parent / "output" / "entry.txt"


def load_joke() -> str:
    joke = ENTRY_PATH.read_text(encoding="utf-8").strip()
    if not joke:
        raise SystemExit("entry.txt is empty — nothing to print")
    return joke


def main() -> None:
    print(load_joke())


if __name__ == "__main__":
    main()
