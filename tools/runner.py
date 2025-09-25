import subprocess, sys
from pathlib import Path


def run(files: list):
    root = Path(__file__).resolve().parent.parent  # project folder
    for f in files:
        script = (root / Path(f))
        rc = subprocess.call([sys.executable, str(script)])

