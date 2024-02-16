def divisible_by_3_and_4_generator(n):
    for i in range(0, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter number N: "))
print("Numbers divisible by both 3 and 4 between 0 and", n, ":", end=" ")
for num in divisible_by_3_and_4_generator(n):
    print(num, end=", ")
