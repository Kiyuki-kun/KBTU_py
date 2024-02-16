def even_numbers_generator(n):
    yield (i for i in range(2, n+1, 2))

n = int(input("Enter a number N: "))
print("Even numbers between 0 and", n, ":", end=" ")
print(*even_numbers_generator(n), sep=", ")