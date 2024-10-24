import math

# Convert degrees to radians
def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

degree = float(input("Input degree: "))
radian = degrees_to_radians(degree)

print(f"Output radian: {radian:.6f}")
