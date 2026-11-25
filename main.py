"""The Word You'd Delete From the Dictionary.

One word to erase forever: inflammable — the word that sounds like it
means "cannot catch fire" and means the exact opposite. Writes the word
to /output/entry.txt. Standard library only; no network, no third-party
packages.
"""

import os

WORD = "inflammable"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(WORD)
    # open() leaves the umask's mode; force 0644 so the scorer can read it.
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
