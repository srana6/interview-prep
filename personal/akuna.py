
def valid(i, j, mountain):
    n = len(mountain)    
    return i >= 0 and i < n and j >= 0 and j < i + 1

def _descent(mountain, path, i, j, memo):
    if not valid(i, j, mountain): return path
    if (i, j) in memo: return memo[(i, j)]
    
    curr = path + mountain[i][j]
    
    left = _descent(mountain, curr, i + 1, j, memo)
    right = _descent(mountain, curr, i + 1, j + 1, memo)
    
    minimum = min(left, right)
    memo[(i, j)] = minimum
    return minimum
    

def descent(mountain):
    if not mountain: return 0    
    size = len(mountain)
    lastrow = size - 1
    memo = {}
        
    for row in mountain:
        print row
        
    _descent(mountain, 0, 0, 0, memo)
    
    return memo[(0, 0)]
    
    


mountain = []
try:
    while True:
        line = [int(x) for x in raw_input().strip().split()]
        mountain.append(line)
except EOFError:
    descent(mountain)
    
    