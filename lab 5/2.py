import re

def match_a_followed_by_2_to_3_b(text):
    pattern = r'ab{2,3}'  
    if re.fullmatch(pattern, text):
        return True
    return False

test_strings = ['a', 'ab', 'abb', 'abbb', 'abbbb', 'ac', 'aabb']
for string in test_strings:
    print(f"Does '{string}' match the pattern? {match_a_followed_by_2_to_3_b(string)}")
