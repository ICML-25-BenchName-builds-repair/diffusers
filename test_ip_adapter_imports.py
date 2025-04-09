#!/usr/bin/env python3
"""
This script checks if the Optional import is used in the ip_adapter.py file.
"""

import ast
import sys

def check_optional_usage(file_path):
    """Check if Optional is used in the given file."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Parse the file
    tree = ast.parse(content)
    
    # Find all imports
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module == 'typing':
            for name in node.names:
                if name.name == 'Optional':
                    imports.append(name.name)
    
    # Find all usages of Optional
    usages = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id == 'Optional':
            usages.append(node.id)
    
    print(f"Found {len(imports)} imports of Optional")
    print(f"Found {len(usages)} usages of Optional")
    
    if len(imports) > 0 and len(usages) == 0:
        print("ERROR: Optional is imported but not used")
        return False
    return True

if __name__ == "__main__":
    file_path = "src/diffusers/loaders/ip_adapter.py"
    if not check_optional_usage(file_path):
        sys.exit(1)
    sys.exit(0)