import re


def match_string(text):
   
    pattern = r'ab*'
    
    
    if re.fullmatch(pattern, text):
        return True
    else:
        return False


test_strings = ['a', 'ab', 'abb', 'ac', 'b', '']
for string in test_strings:
    result = match_string(string)
    print(f"Does '{string}' match the pattern? {result}")
