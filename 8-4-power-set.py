import copy

"""
Write a method to return all subsets of a set

Analysis:
	By definition, a set is collection that holds unique elements, unordered.
	A = [0, 3, 6, 2, 8]

	power set of the set {1, 2, 3} is 
	{{1, 2, 3}, {1, 2}, {1, 3}, {2, 3}, {1}, {2}, {3}, {}}.
"""

def power_set(arr):
	n = len(arr)	
	subsets = [[]]

	# Insert empty
	# Pop previous and duplicate
	# Insert new element into each subset
	# Merge prev with current
	# Insert into subsets

	for elem in arr:		
		new_set = copy.deepcopy(subsets)
		
		for subset in new_set:
			subset.append(elem)
		
		subsets += new_set

	return subsets