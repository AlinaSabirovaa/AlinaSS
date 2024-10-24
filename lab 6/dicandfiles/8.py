import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            os.remove(file_path)
            print(f"File '{file_path}' deleted.")
        else:
            print("File is not writable.")
    else:
        print("File does not exist.")

# Example usage
file_path = 'sample_to_delete.txt'  # Replace with your file path
delete_file(file_path)
