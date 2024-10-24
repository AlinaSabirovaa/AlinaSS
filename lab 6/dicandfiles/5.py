def write_list_to_file(file_path, my_list):
    with open(file_path, 'w') as file:
        for item in my_list:
            file.write(f"{item}\n")
    print(f"List written to '{file_path}'.")

# Example usage
my_list = ['apple', 'banana', 'cherry']
file_path = 'mylist.txt'
write_list_to_file(file_path, my_list)
