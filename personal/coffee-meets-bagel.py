from math import *

# Complete the function below.

MAX = float("inf")
memo = {}
memo[1] = 1
memo[2] = 1


def isPrime(n):
	number = n	

	if number in memo:
		return memo[number]

	smallest = MAX

	# Check if its divisible by 2
	if n % 2 ==0:
		# Not prime

		smallest = 2
		while n % 2 == 0:
			n = n // 2
	
	i = 3	
	while i <= sqrt(n):		
		while n % i == 0:			
			smallest = min(smallest, i)
			n = n // i

		# Jump 2 steps because it might be odd
		i += 2

	# Prime found
	if smallest == MAX:
		smallest = 1

	memo[number] = smallest
	return memo[number]





# Complete the function below.
"""
Analysis:
	If previous bagels are in sorted order
	a linear search would be very slow. It would take O(n)
	We can do better than that in case of a sorted order
	Doing a binary search we can perform that lookup in O(lg n)
""" 

def isPreviouslyMatched(array, target):
	if array:		
		# Helper variables
		start = 0
		end = len(array)
		
		# Traverse logarithmically the array to search the target
		while start < end:
			# Check in the middle
			midIndex = (start + end) // 2
			midValue = array[midIndex]
			
			# Matched found
			if midValue == target:
				return True
			elif midValue < target:
				start = midIndex + 1
			else:
				end = midIndex
				
	# Default, matched is not found
	return False


def  IsNewMatch( match_id,  sorted_old_match_ids):
	matchedBefore = isPreviouslyMatched(sorted_old_match_ids, match_id)    
	if matchedBefore: 
		return False
	
	return True







array = [1, 2, 3, 4, 5, 8, 20, 23, 46]

rest = IsNewMatch(25, array)
print (rest)



result = isPrime(2)

print (result)