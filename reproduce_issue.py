# Script to reproduce the import issue
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

try:
    from diffusers.loaders import FromSingleFileMixin
    print("Successfully imported FromSingleFileMixin")
except ImportError as e:
    print(f"Import error: {e}")

# Try importing the autoencoder_kl module
try:
    from diffusers.models.autoencoders.autoencoder_kl import AutoencoderKL
    print("Successfully imported AutoencoderKL")
except ImportError as e:
    print(f"Import error: {e}")