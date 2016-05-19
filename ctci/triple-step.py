"""
134 - 8.1

A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs.

Hint: 	Multiply: We do this then  this
		Add: We do this or this
"""
import unittest

# Bottom-up approach

def stair_hop(n):
	steps = [1, 2, 3]
	memo = [1] * (n + 1)

	for i in range(1, n + 1):
		memo[i] = 0
		for j in steps:
			if i - j >= 0:
				memo[i] += memo[i - j]
	return memo[n]




# Top-down approach

def _countWays(n, memo):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	elif memo[n] > -1:
		return memo[n]
	else:
		memo[n] = _countWays(n - 1, memo) + _countWays(n - 2, memo) + _countWays(n - 3, memo)

	return memo[n]
	
def countWays(n):
	memo = [-1] * (n + 1)
	return _countWays(n, memo)




class Test(unittest.TestCase):
	data = [
		(4, 7),
		(10, 274),
		(23, 755476),
		(100, 180396380815100901214157639)
	]

	def test_solution(self):
		for (n, expected) in self.data:
			self.assertEqual(stair_hop(n), expected)
			self.assertEqual(countWays(n), expected)
			self.assertEqual(stair_hop(n), countWays(n))

unittest.main()