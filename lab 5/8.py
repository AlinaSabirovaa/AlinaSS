import re

def split_at_uppercase(text):
    return re.findall('[A-Z][^A-Z]*', text)  


test_string = "SplitAtUppercaseLetters"
print(split_at_uppercase(test_string))  
