def get_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
a = int(input("Number 1: "))
b = int(input("Number 2: "))
c = int(input("Number 3: "))

print(get_max(a,b,c))