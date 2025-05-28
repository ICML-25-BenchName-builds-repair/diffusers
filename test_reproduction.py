#!/usr/bin/env python3
"""
Reproduction script for the CI quality check issue.
This script reproduces the exact issue described in the problem statement.
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Run a command and return the result."""
    print(f"\n=== {description} ===")
    print(f"Running: {cmd}")
    
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    print(f"Exit code: {result.returncode}")
    if result.stdout:
        print("STDOUT:")
        print(result.stdout)
    if result.stderr:
        print("STDERR:")
        print(result.stderr)
    
    return result

def main():
    """Main function to reproduce the issue."""
    print("Reproducing the CI quality check issue...")
    
    # Change to the repository directory
    repo_dir = "/lca-workspace/repos/huggingface__diffusers"
    os.chdir(repo_dir)
    print(f"Working directory: {os.getcwd()}")
    
    # Run the exact commands from the CI workflow
    print("\n" + "="*60)
    print("REPRODUCING THE ISSUE")
    print("="*60)
    
    # Run ruff check
    result1 = run_command(
        "ruff check examples tests src utils scripts",
        "Running ruff check (should fail with F401 errors)"
    )
    
    # Run ruff format check
    result2 = run_command(
        "ruff format examples tests src utils scripts --check",
        "Running ruff format check (may also fail)"
    )
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    if result1.returncode != 0:
        print("✗ ruff check FAILED (as expected)")
        if "F401" in result1.stdout:
            print("  - Found F401 unused import errors")
        if "src/diffusers/loaders/single_file_utils.py" in result1.stdout:
            print("  - Errors in single_file_utils.py (as expected)")
    else:
        print("✓ ruff check PASSED (unexpected)")
    
    if result2.returncode != 0:
        print("✗ ruff format check FAILED")
    else:
        print("✓ ruff format check PASSED")
    
    # Show the specific errors we're looking for
    if result1.returncode != 0 and "F401" in result1.stdout:
        print("\nSpecific errors found:")
        lines = result1.stdout.split('\n')
        for line in lines:
            if "F401" in line and "single_file_utils.py" in line:
                print(f"  - {line}")
    
    return result1.returncode != 0 or result2.returncode != 0

if __name__ == "__main__":
    issue_reproduced = main()
    if issue_reproduced:
        print("\n🔴 Issue successfully reproduced!")
        sys.exit(1)
    else:
        print("\n🟢 No issues found.")
        sys.exit(0)