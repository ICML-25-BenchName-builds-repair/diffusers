# Script to check the structure of the __init__.py file
import os

init_file_path = os.path.join('src', 'diffusers', 'loaders', '__init__.py')

with open(init_file_path, 'r') as f:
    content = f.read()

# Check if FromSingleFileMixin is properly exported
if '_import_structure["single_file"] = ["FromSingleFileMixin"]' in content:
    print("FromSingleFileMixin is properly exported in _import_structure")
else:
    print("FromSingleFileMixin is NOT properly exported in _import_structure")

# Check if FromSingleFileMixin is properly imported in the TYPE_CHECKING block
if 'from .single_file import FromSingleFileMixin' in content:
    print("FromSingleFileMixin is properly imported in the TYPE_CHECKING block")
else:
    print("FromSingleFileMixin is NOT properly imported in the TYPE_CHECKING block")

# Check if the import is conditional on is_transformers_available()
lines = content.split('\n')
for i, line in enumerate(lines):
    if '_import_structure["single_file"] = ["FromSingleFileMixin"]' in line:
        # Check if this line is inside an if is_transformers_available() block
        is_conditional = False
        for j in range(i-1, -1, -1):
            if j < 0:
                break
            if 'if is_transformers_available():' in lines[j]:
                is_conditional = True
                break
            if 'if is_torch_available():' in lines[j]:
                break
        
        if is_conditional:
            print("WARNING: FromSingleFileMixin import is conditional on is_transformers_available()")
        else:
            print("GOOD: FromSingleFileMixin import is NOT conditional on is_transformers_available()")
        break