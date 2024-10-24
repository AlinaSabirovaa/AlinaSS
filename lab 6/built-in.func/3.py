def is_palindrome(s):
    return s == s[::-1]  

test_string = "madam"
result = is_palindrome(test_string)
print(f"Is '{test_string}' a palindrome? {result}")
#сзади и спереди читается одинаково
