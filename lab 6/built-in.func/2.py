def count_case(s):
    upper_case = sum(1 for char in s if char.isupper())
    lower_case = sum(1 for char in s if char.islower())
    return upper_case, lower_case

# Example usage
input_string = "Hello World!"
upper, lower = count_case(input_string)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
# сколько аппер и сколько лоуер леттер