# Script to verify that AutoencoderKL can be imported
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

# Mock the transformers import
sys.modules['transformers'] = type('MockTransformers', (), {})
sys.modules['transformers'].AutoFeatureExtractor = type('MockAutoFeatureExtractor', (), {})

# Mock huggingface_hub
sys.modules['huggingface_hub'] = type('MockHuggingfaceHub', (), {})
sys.modules['huggingface_hub.utils'] = type('MockHuggingfaceHubUtils', (), {})
sys.modules['huggingface_hub.utils'].validate_hf_hub_args = lambda x: x

# Try importing the autoencoder_kl module
try:
    from diffusers.models.autoencoders.autoencoder_kl import AutoencoderKL
    print("SUCCESS: AutoencoderKL was imported successfully!")
except ImportError as e:
    print(f"FAILURE: Could not import AutoencoderKL: {e}")