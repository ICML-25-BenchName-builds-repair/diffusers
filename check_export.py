"""
Script to check if FromSingleFileMixin is properly exported in the __init__.py file.
"""
import os

init_file_path = os.path.join('src', 'diffusers', 'loaders', '__init__.py')

with open(init_file_path, 'r') as f:
    lines = f.readlines()

# Check if FromSingleFileMixin is in _import_structure
found_export = False
export_line_number = -1
for i, line in enumerate(lines):
    if '_import_structure["single_file"] = ["FromSingleFileMixin"]' in line:
        found_export = True
        export_line_number = i
        break

if found_export:
    print("FromSingleFileMixin is properly exported in _import_structure")
    
    # Check if it's inside an if is_transformers_available() block
    is_conditional = False
    for i in range(export_line_number, 0, -1):
        if 'if is_transformers_available():' in lines[i]:
            is_conditional = True
            break
        # If we hit another if statement or a blank line, stop looking
        if 'if is_torch_available():' in lines[i] or lines[i].strip() == '':
            break
    
    if is_conditional:
        print("WARNING: FromSingleFileMixin export is conditional on is_transformers_available()")
    else:
        print("GOOD: FromSingleFileMixin export is NOT conditional on is_transformers_available()")
else:
    print("ERROR: FromSingleFileMixin is NOT properly exported in _import_structure")

# Check if FromSingleFileMixin is imported in the TYPE_CHECKING block
found_import = False
import_line_number = -1
for i, line in enumerate(lines):
    if 'from .single_file import FromSingleFileMixin' in line:
        found_import = True
        import_line_number = i
        break

if found_import:
    print("FromSingleFileMixin is properly imported in the TYPE_CHECKING block")
    
    # Check if it's inside an if is_transformers_available() block
    is_conditional = False
    for i in range(import_line_number, 0, -1):
        if 'if is_transformers_available():' in lines[i]:
            is_conditional = True
            break
        # If we hit another if statement or a blank line, stop looking
        if 'if is_torch_available():' in lines[i] or 'if TYPE_CHECKING or DIFFUSERS_SLOW_IMPORT:' in lines[i]:
            break
    
    if is_conditional:
        print("WARNING: FromSingleFileMixin import is conditional on is_transformers_available()")
    else:
        print("GOOD: FromSingleFileMixin import is NOT conditional on is_transformers_available()")
else:
    print("ERROR: FromSingleFileMixin is NOT properly imported in the TYPE_CHECKING block")