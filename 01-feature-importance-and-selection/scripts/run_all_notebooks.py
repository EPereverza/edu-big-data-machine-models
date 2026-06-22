#!/usr/bin/env python3
"""Execute all Lab 01 notebooks (solutions + todo) to generate outputs."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
NOTEBOOKS = [
    "solutions/01_filter_methods_solution.ipynb",
    "solutions/02_wrapper_embedded_solution.ipynb",
    "solutions/03_model_comparison_solution.ipynb",
    "notebooks/01_filter_methods_todo.ipynb",
    "notebooks/02_wrapper_embedded_todo.ipynb",
    "notebooks/03_model_comparison_todo.ipynb",
]


def main() -> None:
    for rel in NOTEBOOKS:
        nb = BASE / rel
        print(f"Executing {rel} ...")
        subprocess.run(
            [
                sys.executable,
                "-m",
                "jupyter",
                "nbconvert",
                "--to",
                "notebook",
                "--execute",
                "--inplace",
                str(nb),
            ],
            cwd=BASE,
            check=True,
        )
    print("All notebooks executed successfully.")


if __name__ == "__main__":
    main()
