"""
You are given a list of size , initialized with zeroes. You have to perform M operations on the list and 
output the maximum of final values of all the  elements in the list. For every operation, you are given three integers , 
 and  and you have to add value  to all the elements ranging from index  to (both inclusive).

Input Format 
First line will contain two integers  and  separated by a single space.
Next  lines will contain three integers ,  and  separated by a single space.
Numbers in list are numbered from  to .

Output Format 
A single line containing maximum value in the updated list.

"""

def crush(N, operations):
    start = [0] * (N + 1)
    end = [0] * (N + 1)

    for (i, j, k) in operations:
        start[i] += k
        end[j] += k

    _sum = 0
    _max = 0

    for i in range(1, N + 1):
        _sum += start[i]
        _max = max(_max, _sum)
        _sum -= end[i]

    return _max

    

    # [0, 120, 100, 100, 100,   0]
    # [0,   0, 100,   0, 100, 220]
    # 320

def read_stdin():
    """

    N, M = list(map(int, input().split()))
    operations = []

    for i in range(M):
        operation = list(map(int, input().split()))
        operations.append(operation) 
        
    print ( crush(N, operations) )

    """


    N = 5
    operations = [
        (1, 2, 100),
        (2, 5, 100),
        (3, 4, 100),
        (1, 5, 20),
        (4, 5, 100)
    ]


    crush(N, operations)
    

read_stdin()



