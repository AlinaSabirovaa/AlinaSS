import os

def check_path(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print(f"Path exists. Filename: {filename}, Directory: {directory}")
    else:
        print("Path does not exist.")

# Example usage
path = './sample.txt'  # Replace with your file path
check_path(path)
