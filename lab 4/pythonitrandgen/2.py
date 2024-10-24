def generate_even_numbers(n):
    for num in range(0, n + 1, 2):  
        yield num

n = int(input("Enter a number (n): "))
even_numbers = generate_even_numbers(n)

print("Even numbers between 0 and", n, ":", end=" ")
print(", ".join(str(num) for num in even_numbers))
