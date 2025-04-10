"""
Test script to verify the FromSingleFileMixin import issue.
"""
import sys

def test_import_from_single_file_mixin():
    try:
        from diffusers.loaders import FromSingleFileMixin
        print(f"Successfully imported FromSingleFileMixin: {FromSingleFileMixin}")
        return True
    except ImportError as e:
        print(f"Error importing FromSingleFileMixin: {e}")
        return False

if __name__ == "__main__":
    print("Testing FromSingleFileMixin import...")
    success = test_import_from_single_file_mixin()
    
    if success:
        print("Import successful!")
        sys.exit(0)
    else:
        print("Import test failed!")
        sys.exit(1)