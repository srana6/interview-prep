"""
Best Time to Buy and Sell Stocks I
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example :

Input : [1 2 6]
Return :  5

"""


class Solution:
	# @param A : tuple of integers
	# @return an integer

	# Time O(n)
	# Space O(1)
	def maxProfit(self, prices):
		if not prices: return 0

		n = len(prices)
		profit = 0		
		smaller = prices[0]

		for i in range(n):
			smaller = min(smaller, prices[i])
			profit = max(profit, prices[i] - smaller)

		return profit

	# Time O(n)
	# Space O(n)
	def maxProfit2(self, prices):
		if not prices: return 0
		n = len(prices)
		memo = [0] * (n + 1)
		profit = 0

		# Store larger numbers from right to left
		for i in reversed(range(n)):
			memo[i] = max(prices[i], memo[i + 1])

			# Calculate profit already knowing largest numbers in right side
			profit = max(profit, memo[i] - prices[i])

		return profit


Solution().maxProfit2([1, 2, 3, 4, 5])

