import re

def match_a_followed_by_anything_ending_in_b(text):
    pattern = r'^a.*b$'  
    if re.fullmatch(pattern, text):
        return True
    return False


test_strings = ['ab', 'a123b', 'abc', 'acb', 'a_b', 'aanythingb', 'a_bbb']
for string in test_strings:
    print(f"Does '{string}' match the pattern? {match_a_followed_by_anything_ending_in_b(string)}")
