def snake_to_camel(snake_str):
    components = snake_str.split('_')  
    return components[0] + ''.join(x.title() for x in components[1:])  

test_string = "this_is_snake_case"
print(snake_to_camel(test_string))  
