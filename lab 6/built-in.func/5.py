def all_true(t):
    return all(t)  

test_tuple = (True, 1, "non-empty", [1, 2, 3])
result = all_true(test_tuple)
print("Are all elements true?", result)
