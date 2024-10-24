import string

def create_text_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            file.write(f"This is file {letter}.")
    print("26 text files created.")

# Example usage
create_text_files()
