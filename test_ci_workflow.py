#!/usr/bin/env python3
"""
Test script to verify that the CI workflow would pass
"""

import subprocess
import sys

def test_ci_quality_check():
    """Test the exact commands that the CI runs"""
    print("Testing CI quality check commands...")
    
    # Test ruff check
    print("Running: ruff check examples tests src utils scripts")
    result1 = subprocess.run([
        "ruff", "check", "examples", "tests", "src", "utils", "scripts"
    ], cwd="/lca-workspace/repos/huggingface__diffusers")
    
    print(f"ruff check exit code: {result1.returncode}")
    
    # Test ruff format --check
    print("Running: ruff format examples tests src utils scripts --check")
    result2 = subprocess.run([
        "ruff", "format", "examples", "tests", "src", "utils", "scripts", "--check"
    ], cwd="/lca-workspace/repos/huggingface__diffusers")
    
    print(f"ruff format --check exit code: {result2.returncode}")
    
    # Both should return 0 for success
    if result1.returncode == 0 and result2.returncode == 0:
        print("✓ CI quality check would PASS")
        return True
    else:
        print("✗ CI quality check would FAIL")
        return False

def test_specific_issue_fixed():
    """Test that the specific issue mentioned in the problem is fixed"""
    print("\nTesting that the specific issue is fixed...")
    
    result = subprocess.run([
        "ruff", "check", "src/diffusers/loaders/ip_adapter.py"
    ], capture_output=True, text=True, cwd="/lca-workspace/repos/huggingface__diffusers")
    
    if result.returncode == 0:
        print("✓ The specific file src/diffusers/loaders/ip_adapter.py passes ruff check")
        
        # Check that the specific error is not present
        if "F401 [*] `typing.Optional` imported but unused" not in result.stdout:
            print("✓ The specific unused import error is gone")
            return True
        else:
            print("✗ The specific unused import error is still present")
            return False
    else:
        print("✗ The specific file still fails ruff check")
        print(f"Output: {result.stdout}")
        return False

if __name__ == "__main__":
    print("Verifying CI workflow would pass...")
    
    test1 = test_ci_quality_check()
    test2 = test_specific_issue_fixed()
    
    if test1 and test2:
        print("\n🎉 SUCCESS: The repository now passes the CI workflow!")
        print("✓ All ruff checks pass")
        print("✓ All formatting checks pass") 
        print("✓ The specific unused import issue is resolved")
        sys.exit(0)
    else:
        print("\n❌ FAILURE: The repository still has issues")
        sys.exit(1)