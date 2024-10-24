import os

def list_contents(path):
    # List all directories
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    print("Directories:", directories)
    
    # List all files
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    print("Files:", files)
    
    # List all directories and files
    all_contents = os.listdir(path)
    print("All contents:", all_contents)

# Example usage
path = '.'  # Current directory
list_contents(path)
