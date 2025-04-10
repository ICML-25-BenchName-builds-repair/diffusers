import sys
print(f"Python version: {sys.version}")

try:
    import diffusers
    print(f"Diffusers version: {diffusers.__version__}")
    
    # Try to import the problematic class
    try:
        from diffusers.models.autoencoders.autoencoder_kl import AutoencoderKL
        print("Successfully imported AutoencoderKL")
    except ImportError as e:
        print(f"Error importing AutoencoderKL: {e}")
    
    # Check if FromSingleFileMixin exists in loaders
    try:
        from diffusers.loaders import FromSingleFileMixin
        print("Successfully imported FromSingleFileMixin")
    except ImportError as e:
        print(f"Error importing FromSingleFileMixin: {e}")
        
    # List all available classes in diffusers.loaders
    import inspect
    from diffusers import loaders
    print("\nAvailable classes in diffusers.loaders:")
    for name, obj in inspect.getmembers(loaders):
        if inspect.isclass(obj):
            print(f"- {name}")
            
except ImportError as e:
    print(f"Error importing diffusers: {e}")