import re

def replace_with_colon(text):
    pattern = r'[ ,.]'  
    return re.sub(pattern, ':', text)

test_string = "Hello, world. This is a test."
print(replace_with_colon(test_string)) 
