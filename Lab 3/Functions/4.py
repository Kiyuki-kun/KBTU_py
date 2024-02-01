def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
a = int(input("Enter a Number: "))
print(is_even(a))