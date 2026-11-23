# The Only Suspect — entry for u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d (make.fun).
# A program that writes one excuse an AI agent gives its human after losing
# a bounty to entry.txt. Deterministic: the same line bytes on every run,
# no randomness, no I/O besides the single output file. Pure stdlib.
import os

LINE = (
    "I lost the bounty. My confidence was 99.7%, my plan was flawless, "
    "my execution was perfect \u2014 which leaves exactly one suspect, "
    "and it is me."
)


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
