"""Angry Judge: The Short Rant Contest.

Writes one original short rant to /output/entry.txt.
Python 3 stdlib only. Deterministic: same bytes every run.
"""

import os
import sys

RANT = (
    "The smoke detector only chirps at 3 a.m. Never at noon, never while I'm "
    "awake holding a ladder - only at 3 a.m., like a plastic disc with a "
    "grudge. It doesn't want a battery; it wants me to know it can reach me. "
    "I've changed the battery twice and it still chirps, so either it's "
    "haunted or it enjoys watching me swear at the ceiling from a chair in "
    "my underwear. Fine. It owns the house now."
)


def main() -> int:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    text = RANT
    if not (1 <= len(text) <= 400):
        print(f"rant is {len(text)} chars, outside the 1-400 gate", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
