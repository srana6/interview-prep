"""
Given a rod of length n inches and a table of prices, determine the maximum revenue obtainable
by cutting up the rod and selling the pieces. 

Note that if the price for a rod of length n is large enough, an optimal solution may require 
no cutting at all.
"""
MAX = float("inf")

def cut_rod(values, N):
	
	revenue = [0 for _ in range(N + 1)]

	for i in range(1, N + 1):
		max_val = -MAX
		for j in range(i):			
			max_val = max(max_val, revenue[i - (j + 1)] + values[j])
		revenue[i] = max_val

	return revenue[N]

values = [2, 3, 7, 8, 9]
N = len(values)

solution = cut_rod(values, N)
print (solution)

