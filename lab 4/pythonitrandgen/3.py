def generate_divisible_by_3_and_4(n):
    for num in range(n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

n = int(input("Enter a number (n): "))
divisible_numbers = generate_divisible_by_3_and_4(n)

print("Numbers divisible by 3 and 4 between 0 and", n, ":", end=" ")
print(", ".join(str(num) for num in divisible_numbers))
