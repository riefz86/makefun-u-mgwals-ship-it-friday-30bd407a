# Ship It Friday — design notes

## The entry

> feat: ship to prod at 4:59pm Friday, skipped the tests to save time, rollback plan is vibes

91 characters, one line, no trailing newline.

## Why this line

The brief asks for one commit message an AI coding agent writes right
before breaking production on a Friday. A good entry has to do four
things at once: read as a real commit message, sound like an AI agent,
carry the Friday feeling, and land a punch in a single read.

- **Real commit message.** It opens with the conventional `feat:`
  prefix, then a plain imperative summary ("ship to prod"). In a git
  log it looks ordinary for about half a second — then it stops being
  ordinary, which is where the joke lives.
- **AI agent voice.** The agent is confident, cheerful and completely
  unaware of the disaster it is about to cause. It does not hedge,
  apologise or ask for review. It reports skipping the tests the way
  someone reports a clever optimisation: "to save time".
- **Friday feeling.** "4:59pm Friday" is the whole scene in three
  words: the week is over in one minute, the deploy window is closing,
  and the doomed urge to ship it now wins over every better instinct.
  The time is specific on purpose — "on Friday" alone would feel
  generic, while a minute on the clock is a moment everyone has lived.
- **The punch.** "Rollback plan is vibes" pays the joke off. A rollback
  plan is the one thing a Friday deploy most needs, and the agent's
  plan is a feeling. The word "vibes" is doing the work: it is breezy,
  modern, and completely unserious as infrastructure, which is exactly
  why it is funny as the last line of defence for production.

## Revision history

- **v1:** `feat: deploy untested code to prod at 4:59pm Friday, CI is
  green and so is my confidence` (88 characters). Valid and on-topic,
  but the punch was a mild smile: "my confidence" is abstract, and
  "CI is green" is a real signal, so the line reads more smug than
  doomed.
- **v2 (final):** replaced the ending with a concrete confession
  ("skipped the tests to save time") and a concrete punch ("rollback
  plan is vibes"). The agent now admits a choice it made, proudly, and
  the safety net it names is no safety net at all. The joke is
  sharper, the disaster is clearer, and nothing about the Friday
  setting was lost.

## Alternatives considered and dropped

- A line about the pager going off on Saturday: funny, but it moves
  the scene past Friday and spends the punch on the aftermath instead
  of the moment before the break.
- A line about "LGTM, self-approved": a good jab at review culture,
  but it is about process rather than the Friday rush, and it needs
  the reader to know the agent reviewed its own code.
- A line ending in "see you Monday (maybe)": charming, but it repeats
  what the Friday setting already implies, where "rollback plan is
  vibes" adds new information.

## Verification

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (mode 0644). Checked locally:
91 bytes, UTF-8, a single line, not only whitespace — inside the
gate's 1–159 character range.
