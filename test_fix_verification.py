#!/usr/bin/env python3
"""
Test script to verify the fix for the unused import issue in ip_adapter.py
"""

import subprocess
import sys

def test_specific_file_fixed():
    """Test that the specific file now passes ruff check"""
    print("Testing that src/diffusers/loaders/ip_adapter.py now passes ruff check...")
    
    result = subprocess.run([
        "ruff", "check", "src/diffusers/loaders/ip_adapter.py"
    ], capture_output=True, text=True, cwd="/lca-workspace/repos/huggingface__diffusers")
    
    print(f"Exit code: {result.returncode}")
    print(f"Stdout: {result.stdout}")
    
    if result.returncode == 0:
        print("✓ File now passes ruff check")
        return True
    else:
        print("✗ File still fails ruff check")
        return False

def test_no_optional_import():
    """Test that Optional is no longer imported"""
    print("\nChecking that Optional is no longer imported...")
    
    with open("/lca-workspace/repos/huggingface__diffusers/src/diffusers/loaders/ip_adapter.py", "r") as f:
        content = f.read()
    
    if "Optional" in content:
        print("✗ Optional is still present in the file")
        return False
    else:
        print("✓ Optional is no longer present in the file")
        return True

def test_dict_union_still_imported():
    """Test that Dict and Union are still imported and used"""
    print("\nChecking that Dict and Union are still properly imported...")
    
    with open("/lca-workspace/repos/huggingface__diffusers/src/diffusers/loaders/ip_adapter.py", "r") as f:
        content = f.read()
    
    # Check import line
    if "from typing import Dict, Union" in content:
        print("✓ Dict and Union are still imported")
        
        # Check usage
        if "Union[str, Dict[str, torch.Tensor]]" in content:
            print("✓ Dict and Union are still used in the code")
            return True
        else:
            print("✗ Dict and Union are not used in the code")
            return False
    else:
        print("✗ Dict and Union import line is incorrect")
        return False

def test_no_unused_import_error():
    """Test that the specific unused import error is gone"""
    print("\nChecking that the specific unused import error is gone...")
    
    result = subprocess.run([
        "ruff", "check", "src/diffusers/loaders/ip_adapter.py"
    ], capture_output=True, text=True, cwd="/lca-workspace/repos/huggingface__diffusers")
    
    if "F401 [*] `typing.Optional` imported but unused" in result.stdout:
        print("✗ The unused Optional import error is still present")
        return False
    else:
        print("✓ The unused Optional import error is gone")
        return True

if __name__ == "__main__":
    print("Verifying the fix for unused import issue...")
    
    tests = [
        test_specific_file_fixed,
        test_no_optional_import,
        test_dict_union_still_imported,
        test_no_unused_import_error
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    if all(results):
        print("\n✓ All verification tests passed - fix is successful!")
        sys.exit(0)
    else:
        print("\n✗ Some verification tests failed - fix needs review")
        sys.exit(1)