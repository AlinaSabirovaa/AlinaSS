def multiply_list(numbers):
    # Using the built-in function reduce to multiply all elements in the list
    from functools import reduce
    return reduce(lambda x, y: x * y, numbers)

# Example usage
numbers = [1, 2, 3, 4]
result = multiply_list(numbers)
print("Product of all numbers in the list:", result)
#умножение чисел