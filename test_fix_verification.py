#!/usr/bin/env python3
"""
Verification script for the fix to the CI quality check issue.
This script verifies that the fix works correctly.
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

def check_file_syntax():
    """Check that the modified file has correct syntax."""
    print("\n=== Checking file syntax ===")
    result = subprocess.run(
        ["python", "-m", "py_compile", "src/diffusers/loaders/single_file_utils.py"],
        capture_output=True, text=True
    )
    
    if result.returncode == 0:
        print("✓ File syntax is correct")
        return True
    else:
        print("✗ File syntax error:")
        print(result.stderr)
        return False

def check_imports_removed():
    """Check that the problematic imports were removed."""
    print("\n=== Checking that unused imports were removed ===")
    
    with open("src/diffusers/loaders/single_file_utils.py", "r") as f:
        content = f.read()
    
    issues = []
    
    # Check for torch import
    if "import torch" in content:
        issues.append("❌ 'import torch' still present")
    else:
        print("✓ 'import torch' removed")
    
    # Check for safetensors import
    if "from safetensors.torch import load_file" in content:
        issues.append("❌ 'from safetensors.torch import load_file' still present")
    else:
        print("✓ 'from safetensors.torch import load_file' removed")
    
    return len(issues) == 0

def main():
    """Main function to verify the fix."""
    print("Verifying the fix for CI quality check issue...")
    
    # Change to the repository directory
    repo_dir = "/lca-workspace/repos/huggingface__diffusers"
    os.chdir(repo_dir)
    print(f"Working directory: {os.getcwd()}")
    
    print("\n" + "="*60)
    print("VERIFYING THE FIX")
    print("="*60)
    
    # Check file syntax
    syntax_ok = check_file_syntax()
    
    # Check imports were removed
    imports_ok = check_imports_removed()
    
    # Run the CI commands that were failing
    result1 = run_command(
        "ruff check examples tests src utils scripts",
        "Running ruff check (should now pass)"
    )
    
    result2 = run_command(
        "ruff format examples tests src utils scripts --check",
        "Running ruff format check (should now pass)"
    )
    
    # Summary
    print("\n" + "="*60)
    print("VERIFICATION SUMMARY")
    print("="*60)
    
    all_good = True
    
    if syntax_ok:
        print("✓ File syntax is correct")
    else:
        print("✗ File syntax has errors")
        all_good = False
    
    if imports_ok:
        print("✓ Unused imports were removed")
    else:
        print("✗ Some unused imports still present")
        all_good = False
    
    if result1.returncode == 0:
        print("✓ ruff check PASSED")
    else:
        print("✗ ruff check FAILED")
        all_good = False
    
    if result2.returncode == 0:
        print("✓ ruff format check PASSED")
    else:
        print("✗ ruff format check FAILED")
        all_good = False
    
    if all_good:
        print("\n🎉 All verifications PASSED! The fix is successful.")
        return True
    else:
        print("\n❌ Some verifications FAILED. The fix needs more work.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)