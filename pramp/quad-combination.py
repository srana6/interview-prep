"""
Given an array of numbers arr and a number S, find 4 different numbers in arr that sum up to S.

Write a function that gets arr and S and returns an array with 4 indices of such numbers in arr, or null if no such combination exists.
Explain and code the most efficient solution possible, and analyze its runtime and space complexity.
"""

def find_array_quad_combination(arr = None, S = None):
	if not arr or not S or len(arr) < 4: return None
	n = len(arr)

	# Hashing preprocessing
	pair_hash = {}
	for i in range(n):
		for j in range(i + 1, n):
			pair_sum = arr[i] + arr[j]
			pair_hash[pair_sum] = pair_hash.get(pair_sum, [])
			pair_hash[pair_sum].append((i, j))

	for pair_sum, pair_a in pair_hash.items():
		remainder = S - pair_sum
		if remainder in pair_hash:
			pair_b = pair_hash.get(remainder)
			combination = find_quad_unique(pair_a, pair_b)
			if combination:
				return combination
	return None

def find_quad_unique(pair_a, pair_b):
	n_a = len(pair_a)
	n_b = len(pair_b)

	for i in range(n_a):
		for j in range(i + 1, n_b):
			if pair_a[i] != pair_b[j]:
				return pair_a[i] + pair_b[j]
	return None


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]	
S = 16
solution = find_array_quad_combination(arr, S)
quad = sum([arr[i] for i in solution])
assert quad == S