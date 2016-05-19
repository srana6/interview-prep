from math import sqrt

# O(sqrt(n))

def isPrime(num):
    n = int(sqrt(num))

    for i in range(2, n + 1):
        if num % i == 0:
            return False
    return True

num = 101101331
print (isPrime(num))