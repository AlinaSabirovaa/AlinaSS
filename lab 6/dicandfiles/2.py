import os

def check_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    
    print(f"Path exists: {exists}")
    print(f"Readable: {readable}")
    print(f"Writability: {writable}")
    print(f"Executability: {executable}")

# Example usage
path = './'  # Current directory
check_access(path)
