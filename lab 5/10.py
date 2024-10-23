import re

def camel_to_snake(camel_str):
    
    snake_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()
    return snake_str


test_string = "convertCamelCaseToSnakeCase"
print(camel_to_snake(test_string))  
