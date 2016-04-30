"""
Analysis:
	Need to find a longest subset such that 
		[a0 , a1, a2, ... , an]    aj < ai

	Recurrence:
		LIS =   {

			1 + max[  arr(j)  ]     if   aj < ai

			1  						any other

		}
"""

def longest_increasing_subsequence(arr):
    if not arr: return 0
    n = len(arr)
    
    memo = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                memo[i] = max(memo[i], 1 + memo[j])


    longest = 1
    for i in range(n):
        longest = max(longest, memo[i])
        
    print (longest)


arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
longest_increasing_subsequence(arr)

