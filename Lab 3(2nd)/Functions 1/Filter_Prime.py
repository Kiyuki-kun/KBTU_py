def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))

'''
numbers_str = input("Enter numbers separated by spaces: ")
numbers = list(map(int, numbers_str.split()))
prime_numbers = filter_prime(numbers)
print("Prime numbers in the list:", prime_numbers)
'''