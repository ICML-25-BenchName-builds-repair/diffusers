import sys
import importlib

# Try to import the FromSingleFileMixin class
try:
    from diffusers.loaders import FromSingleFileMixin
    print("Successfully imported FromSingleFileMixin")
except ImportError as e:
    print(f"Failed to import FromSingleFileMixin: {e}")

# Try to import the AutoencoderKL class which imports FromSingleFileMixin
try:
    from diffusers.models.autoencoders.autoencoder_kl import AutoencoderKL
    print("Successfully imported AutoencoderKL")
except ImportError as e:
    print(f"Failed to import AutoencoderKL: {e}")
    
# Try to import the ControlNetModel class which also imports FromSingleFileMixin
try:
    from diffusers.models.controlnet import ControlNetModel
    print("Successfully imported ControlNetModel")
except ImportError as e:
    print(f"Failed to import ControlNetModel: {e}")