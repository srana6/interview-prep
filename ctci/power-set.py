"""
135 - 8.4
Write a method to return all subsets of a set
"""


# O(n2 powerN)
def power_set(arr):
	memo = [[]]	
	for num in arr:		
		for i in range(len(memo)):			
			memo.append(memo[i] + [num])
	return memo

print (power_set(['a', 'b', 'c', 'd', 'f', 'g', 'h']))