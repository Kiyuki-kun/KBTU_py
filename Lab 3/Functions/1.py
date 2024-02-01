def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)
    
a = int(input("Enter a Number: "))    
print(calculate_factorial(a))