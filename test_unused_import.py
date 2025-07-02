#!/usr/bin/env python3
"""
Test script to reproduce the unused import issue in ip_adapter.py
"""

import subprocess
import sys

def test_ruff_check():
    """Test that ruff check fails due to unused import"""
    print("Running ruff check on src/diffusers/loaders/ip_adapter.py...")
    
    result = subprocess.run([
        "ruff", "check", "src/diffusers/loaders/ip_adapter.py"
    ], capture_output=True, text=True, cwd="/lca-workspace/repos/huggingface__diffusers")
    
    print(f"Exit code: {result.returncode}")
    print(f"Stdout: {result.stdout}")
    print(f"Stderr: {result.stderr}")
    
    # Check if the specific error is present
    expected_error = "F401 [*] `typing.Optional` imported but unused"
    if expected_error in result.stdout:
        print("✓ Successfully reproduced the unused import issue")
        return True
    else:
        print("✗ Failed to reproduce the unused import issue")
        return False

def test_ruff_check_all():
    """Test that ruff check fails on the entire codebase"""
    print("\nRunning ruff check on entire codebase...")
    
    result = subprocess.run([
        "ruff", "check", "examples", "tests", "src", "utils", "scripts"
    ], capture_output=True, text=True, cwd="/lca-workspace/repos/huggingface__diffusers")
    
    print(f"Exit code: {result.returncode}")
    
    # Check if the specific error is present
    expected_error = "src/diffusers/loaders/ip_adapter.py:15:26: F401 [*] `typing.Optional` imported but unused"
    if expected_error in result.stdout:
        print("✓ Successfully reproduced the CI failure")
        return True
    else:
        print("✗ Failed to reproduce the CI failure")
        return False

if __name__ == "__main__":
    print("Testing unused import reproduction...")
    
    # Test individual file
    success1 = test_ruff_check()
    
    # Test entire codebase (like CI)
    success2 = test_ruff_check_all()
    
    if success1 and success2:
        print("\n✓ All tests passed - issue successfully reproduced")
        sys.exit(0)
    else:
        print("\n✗ Some tests failed - issue not fully reproduced")
        sys.exit(1)