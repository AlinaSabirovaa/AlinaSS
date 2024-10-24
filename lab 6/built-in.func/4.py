import time
import math

def delayed_square_root(value, milliseconds):
    # Convert milliseconds to seconds
    time.sleep(milliseconds / 1000)  
    return math.sqrt(value)

value = 25100
delay = 2123
result = delayed_square_root(value, delay)
print(f"Square root of {value} after {delay} milliseconds is {result}")
# ждут 2.123 сек перед оутпут