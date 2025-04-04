# Test script to verify FromSingleFileMixin import
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

# Mock the transformers import
sys.modules['transformers'] = type('MockTransformers', (), {})
sys.modules['transformers'].AutoFeatureExtractor = type('MockAutoFeatureExtractor', (), {})

# Try importing FromSingleFileMixin directly
try:
    from diffusers.loaders import FromSingleFileMixin
    print("Successfully imported FromSingleFileMixin")
    print("Fix is working!")
except ImportError as e:
    print(f"Import error: {e}")
    print("Fix is NOT working!")