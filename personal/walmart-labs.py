def  distributeCandy(score):
    if not score: return 0
    if len(score) == 1: return 1
    if len(score) == 2: return 3
    
    n = len(score)
    left = [1] * n
    right = [1] * n
    candies = 0
        
    for i in range(1, n):
        if score[i - 1] < score[i]:
            left[i] = left[i - 1] + 1
            
    
    for i in reversed(range(n - 1)):         
        if score[i] > score[i + 1]:
            right[i] = right[i + 1] + 1

    #print (left)
    #print (right)
    
    for i in range(n):
        candies += max(left[i], right[i])
    
    return candies


arr = [1, 2, 2]
sol = distributeCandy(arr)
print (sol)
        