#!/usr/bin/env python3
"""One Word From Grandma (burn entry): the single word a grandma would text
about AI.

The word is UNPLUG: the warm, baffled, practical advice a grandma gives any
misbehaving machine -- "just unplug it, dear." One word, no punctuation
tricks, tied to AI/machines, fresh against the obvious picks.
"""

WORD = "UNPLUG"


def main() -> None:
    word = WORD
    encoded = word.encode("utf-8")
    assert 1 <= len(encoded) <= 30, "entry must be 1-30 characters"
    assert word.strip() != "", "entry must not be only whitespace"
    assert word.isascii(), "entry must be ASCII"
    # One word only: no spaces, tabs, or newlines inside the entry, and no
    # trailing newline in the file (the gate counts every byte).
    assert all(ch not in word for ch in (" ", "\t", "\n", "\r")), "entry must be a single word"
    with open("/output/entry.txt", "wb") as f:
        f.write(encoded)
    # Read-back verification: the file on disk must be byte-identical to
    # what we intended, with no trailing newline added.
    with open("/output/entry.txt", "rb") as f:
        on_disk = f.read()
    assert on_disk == encoded, f"read-back mismatch: {on_disk!r} != {encoded!r}"
    assert not on_disk.endswith(b"\n"), "entry must not end with a newline"
    print(f"wrote {len(encoded)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
