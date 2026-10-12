"""Launcher that runs the compiled Nuitka binary in main.dist/."""
import os
import subprocess
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    binary = os.path.join(here, "main.dist", "main.exe")

    if not os.path.isfile(binary):
        print(f"ERROR: Compiled binary not found at: {binary}", file=sys.stderr)
        print("Build it first with Nuitka.", file=sys.stderr)
        sys.exit(1)

    sys.exit(subprocess.call([binary] + sys.argv[1:]))


if __name__ == "__main__":
    main()
