"""
Test script to verify the specific import issue.
"""
import sys

def test_specific_import():
    try:
        # Import the specific class directly
        from diffusers.models.autoencoders.autoencoder_kl import AutoencoderKL
        print(f"Successfully imported AutoencoderKL: {AutoencoderKL}")
        return True
    except Exception as e:
        print(f"Error importing AutoencoderKL: {e}")
        return False

if __name__ == "__main__":
    print("Testing specific import...")
    success = test_specific_import()
    
    if success:
        print("Import successful!")
        sys.exit(0)
    else:
        print("Import test failed!")
        sys.exit(1)