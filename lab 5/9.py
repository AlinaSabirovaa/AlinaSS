import re

def insert_spaces(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)  


test_string = "InsertSpacesBetweenCapitalWords"
print(insert_spaces(test_string))  
