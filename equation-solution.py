"""
Print all positive integer solutions to the equation a^3 + b^3 = c^3 + d^3
where a, b, c, and d are integers between 1 and 100.
"""

def solution():
    n = 1000
    hash_table = {}

    for c in range(1, n + 1):
        for d in range(1, n + 1):
            result = pow(c, 3) + pow(d, 3)
            
            if result not in hash_table:
                hash_table[result] = []
            hash_table[result].append( [c, d] )

    for result in hash_table:       
        for i, pair1 in enumerate(hash_table[result]) :
            for j, pair2 in enumerate(hash_table[result]) :
                print (pair1, pair2)

solution()