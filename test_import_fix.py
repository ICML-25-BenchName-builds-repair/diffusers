"""
Test script to verify the fix for the FromSingleFileMixin import issue.
This script patches the necessary dependencies to isolate the specific issue.
"""
import sys
import os
from unittest.mock import MagicMock

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

# Create a more comprehensive mock for the dependencies
class MockModule:
    pass

# Mock transformers
mock_transformers = MockModule()
mock_transformers.AutoFeatureExtractor = type('MockAutoFeatureExtractor', (), {
    'from_pretrained': lambda *args, **kwargs: None
})
sys.modules['transformers'] = mock_transformers

# Mock huggingface_hub more completely
mock_hub = MockModule()
mock_hub.utils = MockModule()
mock_hub.constants = MockModule()
mock_hub.constants.HF_HOME = "/tmp/huggingface"
mock_hub.constants.HUGGINGFACE_HUB_CACHE = "/tmp/huggingface/hub"
mock_hub.utils.validate_hf_hub_args = lambda func: func
sys.modules['huggingface_hub'] = mock_hub
sys.modules['huggingface_hub.utils'] = mock_hub.utils
sys.modules['huggingface_hub.constants'] = mock_hub.constants

# Mock torch
mock_torch = MockModule()
mock_torch.nn = MockModule()
mock_torch.nn.Module = type('Module', (), {})
sys.modules['torch'] = mock_torch
sys.modules['torch.nn'] = mock_torch.nn

# Patch the import_utils functions
def patch_import_utils():
    import diffusers.utils.import_utils as import_utils
    # Patch the availability checks
    import_utils.is_torch_available = lambda: True
    import_utils.is_transformers_available = lambda: True
    import_utils._torch_available = True
    import_utils._transformers_available = True

# Now try to import FromSingleFileMixin
try:
    patch_import_utils()
    from diffusers.loaders import FromSingleFileMixin
    print("SUCCESS: FromSingleFileMixin was imported successfully!")
    print("The fix is working correctly.")
except ImportError as e:
    print(f"FAILURE: Could not import FromSingleFileMixin: {e}")
    print("The fix is NOT working correctly.")