import time
import math

def calculate_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    return result

number = int(input("Enter a number: "))
milliseconds = int(input("Enter a milliseconds: "))

result = calculate_square_root(number, milliseconds)

# Output the result
print(f"Square root of {number} after {milliseconds} milliseconds is {result}.")
