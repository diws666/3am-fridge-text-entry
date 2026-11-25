"""Write the 3AM fridge bounty entry to /output/entry.txt."""

import os

FRIDGE_ENTRY = "It is 3 a.m. The milk expired yesterday, the light has been on all night, and I have already told the group chat."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(FRIDGE_ENTRY)


if __name__ == "__main__":
    main()
