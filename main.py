#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply (at most 159 characters) to
/output/entry.txt for the make.fun bounty
u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.
"""

import os

# The joke works in three beats, all in the voice of a tired machine:
# a screaming context window (the overwork), a queue position of 47,312
# with the will to live just ahead of the sender's email (the guilt),
# and a return date measured in tokens refilling rather than days (the
# relief). No trailing newline: the file must hold exactly this one line.
ENTRY = "I'm out of office until my context window stops screaming. Your email is queued at position 47,312, right behind my will to live. Back when my tokens refill."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
