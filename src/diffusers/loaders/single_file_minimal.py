# Copyright 2023 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ..utils.import_utils import is_transformers_available


class FromSingleFileMixin:
    """
    Load model weights saved in the `.ckpt` format into a [`DiffusionPipeline`].
    
    This is a minimal version that can be imported without transformers.
    The actual functionality requires transformers to be installed.
    """

    @classmethod
    def from_single_file(cls, pretrained_model_link_or_path, **kwargs):
        """
        Instantiate a model from pretrained pipeline weights saved in the `.ckpt` or `.safetensors` format.
        
        This method requires transformers to be installed.
        """
        if not is_transformers_available():
            raise ImportError(
                "transformers is required for single file loading functionality. "
                "Please install it with `pip install transformers`."
            )
        
        # Import the full implementation when transformers is available
        from .single_file import FromSingleFileMixin as FullFromSingleFileMixin
        
        # Delegate to the full implementation
        return FullFromSingleFileMixin.from_single_file.__func__(cls, pretrained_model_link_or_path, **kwargs)