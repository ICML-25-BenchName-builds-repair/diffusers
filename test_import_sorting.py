#!/usr/bin/env python3

import subprocess
import sys

def main():
    """Run ruff check on the problematic file and report the result."""
    file_path = "examples/community/ip_adapter_face_id.py"
    
    # Run ruff check on the file
    result = subprocess.run(
        ["ruff", "check", file_path],
        capture_output=True,
        text=True
    )
    
    print(f"Exit code: {result.returncode}")
    print("STDOUT:")
    print(result.stdout)
    print("STDERR:")
    print(result.stderr)
    
    return result.returncode

if __name__ == "__main__":
    sys.exit(main())