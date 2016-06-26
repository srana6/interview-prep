"""

Consider four numbers: A, B, C, and K. You must change at most  bits in A and B to form the numbers A' and B' satisfying the equation  A' | B' = C. 
Here, the | symbol denotes the bitwise OR operation.

Given Q sets of the numbers defined above, find and print the respective values of A' and B' on new lines; if no such value exists, print -1  
instead. If there are multiple solutions, make A' as small as possible; if there are still multiple solutions, make B' as small as possible.

Note:

A, B, and C are given in Hexadecimal (base 16), and  is given in decimal (base 10).

If number of bits changed in  is  and number of bits changed in B is , than  must be smaller or equal to .

"""

def get_ith(num, i):
    temp = num & (1 << i)
    return temp >> i


def toggle_ith(num, i):
    return num ^ (1 << i)


def minimize(A, B, C, K):
    maximum = max(A, B)
    maximum_str = bin(maximum)[2:]
    i = len(maximum_str) - 1
    while i and K:
        a = get_ith(A, i)
        b = get_ith(B, i)

        if a & b:
            A = toggle_ith(A, i)

        K -= 1
        i -= 1
    return (A, B)


def solution(A, B, C, K):
    i = 0        
    while A | B != C and K:
        c = get_ith(C, i)
        a, b = get_ith(A, i), get_ith(B, i)

        while a | b != c:
            _A = toggle_ith(A, i)
            _B = toggle_ith(B, i)

            if _A <= A:
                A = _A
                a = get_ith(A, i)
            else:
                B = _B
                b = get_ith(B, i)       
            K -= 1
        i += 1        

    if A | B == C and K >= 0:
        if K:
            A, B = minimize(A, B, C, K)

        print (hex(A)[2:].upper())
        print (hex(B)[2:].upper())
    else:
        print (-1)



def read_stdin():
    Q = int(input())    

    for i in range(Q):
        K = int(input())
        A = int(input(), 16)
        B = int(input(), 16)
        C = int(input(), 16)
        solution(A, B, C, K)
    
    read_stdin()



A = int("11111011111111110011011", 2)
B = int("10100100111010111", 2)
C = int("110010111111010111", 2)
K = 40

print (hex(A)[2:].upper(), hex(B)[2:].upper(), hex(C)[2:].upper())

solution(A, B, C, K)

"""
  101011
10011111
 1011000

10111001
 1000000
 1011010

2
10010001
10111110
10101000

"""
