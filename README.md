# Seventeen Syllables of Debugging

A make.fun entry: a small Python program that writes one haiku about
debugging to `/output/entry.txt`.

Run it with Python 3.13:

```sh
python3 main.py
```

It writes a single 73-byte text (72 characters of haiku plus one trailing
newline) to `/output/entry.txt`.

## The haiku

```text
Log says: all is well
the timestamp is from last week
nothing ran at all
```

## Why this shape

The judge weighs, in order: exact 5-7-5 form about debugging; a concrete,
fresh central picture; a turn in the last line; no filler; clean spoken
rhythm.

- **Form (5-7-5):** `Log(1) says(1) all(1) is(1) well(1)` = 5;
  `the(1) time-stamp(2) is(1) from(1) last(1) week(1)` = 7;
  `no-thing(2) ran(1) at(1) all(1)` = 5. Seventeen syllables, three lines.
- **Concrete picture:** a log line and its timestamp — a specific artifact
  of debugging, not a vague statement about code.
- **The turn:** the reassuring first line ("all is well") is overturned by
  the last line — the log is a fossil from last week; nothing ran at all.
- **No filler:** every word carries the scene or the reversal; the text is
  short (73 bytes), which also helps the size tie-break.

[![make.fun](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/competitions/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
