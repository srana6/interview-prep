"""
UBER Interview 


Given an array that contain 3 distinct numbers, where there exists at least one instance of each number.
Find where the boundaries are in the array.

You can assume the array is sorted.

    Analysis:

        

    IN: [1,1,1,  __       { 1__, 5   ,5, X     _}, 5          _     ,5,5,     8,8] 
    [                            |                  ]                        ||
                                   2
                                  [                                                 ]
                                  
                                                                             ||i + 1  888888 end 

"""
# Array with at least 1 instance of three distinct numbers (sorted)

# OUT: [2, 6]
# The boundaries, specifically the index of the number left of the boundary


# Brute force solution
# result = []
# Time O(n)
# Space (1)



# Solution 
# Time O(lg n)
# Run binary search twice  O( lg n)

# 1st lookup
#   first boundary
# 2nd lookup
#     boundary as guidance
#     check left side : start 1111  end
#           right 
#                    run binary search there




def search_boundary(arr, start, end):   
    while start < end:
        midIndex = start + end // 2
        midValue = arr[midIndex]
        
        if midIndex - 1 >= 0 and arr[midIndex - 1] != midValue:
            return midIndex 
            
        if midIndex + 1 < len(arr) and arr[midIndex + 1] != midValue:
            return midIndex # + 1       
                             
        
        if arr[start] != midValue:
            end = midIndex - 1
        
        else:
            start = midIndex + 1
    return -1
    
# [1,1,1,2,2 ,3,3]
# [2,4]

# arr[2] -> 1

def get_boundaries(arr):    
    start = 0
    end = len(arr)
    firstB = search_boundary(arr, start, end)
    secondB = -1
    
    if arr[firstB] == arr[start]:
        secondB = search_boundary(arr, firstB + 1, end)
    else:

        secondB = search_boundary(arr, start, firstB)  

    return sort([firstB, secondB]) 
    


# INPUT: 2 arrays de cualquier length + 1 numero = X
# OUTPUT: 1 indice de cada array such that arr1[index1] + arr2[index2] = X



