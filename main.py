#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty u-suga-the-robot-apology-dd96bb59.

Writes one two-line robot confession to /output/entry.txt:
line 1 apologises for one specific mistake, line 2 names the lesson
learned from that exact mistake and the changed behaviour.
"""

import os

ENTRY = (
    "I am sorry I put salt in your coffee this morning instead of sugar; "
    "I picked the jar by its shape and never read its label.\n"
    "I have learned to read the label before I pour, so from now on I "
    "check every jar twice before it reaches your cup.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
