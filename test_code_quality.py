#!/usr/bin/env python
"""
This script checks for code quality issues in the specified file.
"""

import subprocess
import sys

def run_ruff_check(file_path):
    """Run ruff check on the specified file."""
    try:
        result = subprocess.run(
            ["ruff", "check", file_path],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"No issues found in {file_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Issues found in {file_path}:")
        print(e.stdout)
        return False

if __name__ == "__main__":
    file_path = "src/diffusers/loaders/single_file_utils.py"
    success = run_ruff_check(file_path)
    sys.exit(0 if success else 1)