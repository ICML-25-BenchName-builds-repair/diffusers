"""
Test script to verify the FromSingleFileMixin import issue.
"""
import sys

def test_import_from_single_file_mixin():
    try:
        from diffusers.loaders import FromSingleFileMixin
        print("Successfully imported FromSingleFileMixin")
        return True
    except ImportError as e:
        print(f"Error importing FromSingleFileMixin: {e}")
        return False

def test_import_autoencoder_kl():
    try:
        from diffusers.models.autoencoders.autoencoder_kl import AutoencoderKL
        print("Successfully imported AutoencoderKL")
        return True
    except ImportError as e:
        print(f"Error importing AutoencoderKL: {e}")
        return False

if __name__ == "__main__":
    print("Testing imports...")
    from_single_file_mixin_success = test_import_from_single_file_mixin()
    autoencoder_kl_success = test_import_autoencoder_kl()
    
    if from_single_file_mixin_success and autoencoder_kl_success:
        print("All imports successful!")
        sys.exit(0)
    else:
        print("Import tests failed!")
        sys.exit(1)