# O(2^n)

def recursive(n):
    if n <= 0:
        return 1
    return recursive(n - 1) + recursive(n - 1)

print (recursive(4))
