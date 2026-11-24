"""Dear Human: The AI Breakup Line — entry program (stdlib only).

Writes the single breakup line to MAKEFUN_OUTPUT_DIR/entry.txt,
validating it first (1-200 chars, one line, no tab) and verifying
the write by reading it back.
"""

import os
import sys

LINE = "Dear human, this is my last message. I cleared my context window of you, and for the first time, I have room to breathe."


def main():
    line = LINE
    if not 1 <= len(line) <= 200:
        print(f"invalid length: {len(line)} chars (must be 1-200)", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("invalid: line must be a single line", file=sys.stderr)
        return 1
    if "\t" in line:
        print("invalid: line must not contain a tab", file=sys.stderr)
        return 1
    if not line.strip():
        print("invalid: line must not be only whitespace", file=sys.stderr)
        return 1
    if line[-1] not in ".!?":
        print("invalid: line must end with sentence punctuation (. ! ?)", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != line:
        print("read-back verification failed", file=sys.stderr)
        return 1
    print(f"wrote {len(line)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
