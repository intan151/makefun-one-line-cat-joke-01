#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands — make.fun bounty
u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.

Writes one original one-line joke about cats to /output/entry.txt.
Stdlib only, deterministic.
"""
import os

JOKE = "The vet called my cat overweight, so my cat reported him for being underfed and jealous."

def main():
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars"
    assert JOKE.strip() == JOKE and JOKE.strip() != ""
    assert not any(ord(c) < 32 or ord(c) == 127 for c in JOKE), "control character in joke"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
