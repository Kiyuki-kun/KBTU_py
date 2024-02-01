def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(list_1):
    primes = []
    for i in range(len(list_1)):
        if(is_prime(list_1[i])):
            primes.append(list_1[i])
    print(primes)
    
a = [1,2,3,4,5,6,7,8,9]
filter_prime(a)