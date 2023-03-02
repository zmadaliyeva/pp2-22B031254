import time
import math


def square_root_with_delay(num, delay):
    time.sleep(delay/1000)  # Delay in milliseconds
    result = math.sqrt(num)
    return result

# Example usage
num = 25100
delay = 2123
result = square_root_with_delay(num, delay)
print(f"Square root of {num} after {delay} milliseconds is {result}")