"""
Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents),
and pennies (1 cent), write a code to calculate the number of ways representing N cents.

Analysis:
	This seems as the common coin change problem

	Solve with DP

	Brute force solution:
		Try every possible combination 

"""

# This calculates the minimum coins needed
def valid(i, N):
	return i >=0 and i < N

def coin_change(N):
	coins = [1, 2, 3]

	MAX = float("inf")
	memo = [MAX] * (N + 1)
	memo[0] = 0
	
	for money in range(N + 1):
		for coin in coins:
			if valid(money - coin, N):
				memo[money] = min(memo[money], memo[money - coin] + 1)


	return (memo[N])


# Calculates number of ways to have that. Time complexity is huge because it tries all combinations
def _makeChange(amount, denoms, index, memo):	
	if memo[amount][index] > 0: return memo[amount][index]
	if index >= len(denoms) - 1: return 1

	denomAmount = denoms[index]
	ways = 0

	i = 0
	while (i * denomAmount) <= amount:
		remaining = amount - i * denomAmount
		print (remaining)
		ways += _makeChange(remaining, denoms, index + 1, memo)
		i += 1

	memo[amount][index] = ways

	for row in memo:
		print (row)
		
	return ways

def makeChange(N):
	denoms = [3, 2, 1]
	memo = [[0] * (len(denoms) + 1) for _ in range(N + 1)]

	

	return _makeChange(N, denoms, 0, memo)


print ("coins", coin_change(4))
print ("change", makeChange(4))