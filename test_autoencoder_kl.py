"""
Test script to verify the AutoencoderKL import issue.
"""
import sys

def test_import_autoencoder_kl():
    try:
        from diffusers.models.autoencoders.autoencoder_kl import AutoencoderKL
        print("Successfully imported AutoencoderKL")
        return True
    except ImportError as e:
        print(f"Error importing AutoencoderKL: {e}")
        return False

if __name__ == "__main__":
    print("Testing AutoencoderKL import...")
    success = test_import_autoencoder_kl()
    
    if success:
        print("Import successful!")
        sys.exit(0)
    else:
        print("Import test failed!")
        sys.exit(1)