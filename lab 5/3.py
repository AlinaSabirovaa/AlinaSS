import re

def match_lowercase_joined_with_underscore(text):
    pattern = r'^[a-z]+_[a-z]+$'  
    if re.fullmatch(pattern, text):
        return True
    return False


test_strings = ['abc_def', 'ABC_DEF', 'abc_def_ghi', 'abcdef', 'abc_']
for string in test_strings:
    print(f"Does '{string}' match the pattern? {match_lowercase_joined_with_underscore(string)}")
