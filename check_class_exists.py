# Script to check if the FromSingleFileMixin class is defined in the single_file.py file
import os

single_file_path = os.path.join('src', 'diffusers', 'loaders', 'single_file.py')

with open(single_file_path, 'r') as f:
    content = f.read()

if 'class FromSingleFileMixin:' in content:
    print("FromSingleFileMixin class is defined in single_file.py")
else:
    print("FromSingleFileMixin class is NOT defined in single_file.py")