#!/usr/bin/env python3
"""
Test script to verify import sorting in ip_adapter_face_id.py
"""

import subprocess
import sys

def main():
    # Run ruff check on the file
    result = subprocess.run(
        ["ruff", "check", "examples/community/ip_adapter_face_id.py"],
        capture_output=True,
        text=True
    )
    
    print("Exit code:", result.returncode)
    print("Output:")
    print(result.stdout)
    
    if result.returncode != 0:
        print("Error detected in imports. Let's fix it.")
        # Run ruff with --fix to see what it would do
        fix_result = subprocess.run(
            ["ruff", "check", "examples/community/ip_adapter_face_id.py", "--fix", "--show-fixes"],
            capture_output=True,
            text=True
        )
        print("\nFix suggestion:")
        print(fix_result.stdout)
        return 1
    else:
        print("No import issues detected!")
        return 0

if __name__ == "__main__":
    sys.exit(main())