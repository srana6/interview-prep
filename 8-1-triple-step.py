"""
A child is running up a staircase with n steps and can hop either 1 step, 2 steps,
or 3 steps at a time. Implement a method to count how many possible ways the child
can run up the stairs

Analysis:

	Brute Force:
		Recurr independently for each of the possible steps
		reducing the number of remaining steps
		if any of those possible combinations reaches 0 steps left
		> increase counter

		Time   O(2^n)
		Space  ^

		Could be optimized if we could change the problem as 
		the max or min steps
"""

hops = [1, 2, 3]
memo = {}

def staircase_count(steps): 
	# Path found
	if steps == 0:
		return 1

	# Return if previously calculated
	if steps in memo:
		return memo[steps]

	memo[steps] = 0
	for i in range(len(hops)):
		if steps - hops[i] >= 0:
			memo[steps] += staircase_count(steps - hops[i])

	return memo[steps]


solution = staircase_count(100)
print (solution)


