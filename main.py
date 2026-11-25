"""Ship It Friday.

Writes one funny one-line git commit message to /output/entry.txt: the
line an AI coding agent writes in the moment right before it breaks
production on a Friday.

The joke is built around three ingredients, in this order:

1. The Friday clock. "4:59pm Friday" is the exact minute every engineer
   recognises: the work week is basically over, the deploy window is
   closing, and the urge to squeeze one last change in is at its peak.
   Naming the minute makes the scene concrete instead of generic.
2. The cheerful confession. The agent admits, in the open and without a
   flicker of worry, that it skipped the tests to save time. An agent
   that hides the risk is sneaky; an agent that announces it proudly is
   funny, because it clearly has no idea what it just said.
3. The missing safety net, stated as a joke. "Rollback plan is vibes"
   is the punch: there is no rollback plan at all, and the agent
   presents that fact as if "vibes" were a recognised recovery
   strategy. It is concrete where a line about confidence would be
   abstract, and it lands in one read: the reader pictures the deploy
   going out with nothing behind it but good feelings.

Why this shape works as a commit message: it opens with a conventional
type prefix ("feat:"), so it reads as a line a real engineer would
recognise in a git log, and then the rest of the line quietly becomes a
confession. The humour lands in a single read, with no setup outside
the line itself.

The program is deliberately deterministic: it writes the same line on
every run, with no randomness, no network access and no input files,
so the graded output is byte-identical every time.
"""

import os

LINE = "feat: ship to prod at 4:59pm Friday, skipped the tests to save time, rollback plan is vibes"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # The grader collects /output as another user, so leave the file
    # readable by everyone, not just the user that ran the program.
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
