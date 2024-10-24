def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        print(f"Number of lines in '{file_path}': {len(lines)}")

# Example usage
file_path = 'sample.txt'  # Replace with your file path
count_lines(file_path)
