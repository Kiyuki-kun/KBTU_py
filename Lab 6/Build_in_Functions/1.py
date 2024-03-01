from functools import reduce

def multiply_list(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

if numbers:
    result = multiply_list(numbers)
    print("Result of multiplying all numbers:", result)
else:
    print("No numbers provided.")

