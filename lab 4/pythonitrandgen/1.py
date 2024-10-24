def generate_squares(N):
    for num in range(1, N + 1):
        yield num * num

N = 5
for square in generate_squares(N):
    print(square)
