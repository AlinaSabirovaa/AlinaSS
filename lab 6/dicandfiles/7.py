def copy_file(source_path, dest_path):
    with open(source_path, 'r') as source_file:
        with open(dest_path, 'w') as dest_file:
            dest_file.write(source_file.read())
    print(f"Contents copied from '{source_path}' to '{dest_path}'.")

# Example usage
source_path = 'source.txt'  # Replace with your file path
dest_path = 'destination.txt'
copy_file(source_path, dest_path)
