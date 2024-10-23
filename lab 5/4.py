import re

def match_uppercase_followed_by_lowercase(text):
    pattern = r'^[A-Z][a-z]+$'  
    if re.fullmatch(pattern, text):
        return True
    return False


test_strings = ['Abc', 'aBc', 'ABC', 'Ab', 'A', 'AbCd']
for string in test_strings:
    print(f"Does '{string}' match the pattern? {match_uppercase_followed_by_lowercase(string)}")
