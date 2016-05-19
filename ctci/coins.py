"""
Given a list of N coins, their values (V1, V2, … , VN), and the total sum S. 
Find the minimum number of coins the sum of which is S 
(we can use as many coins of one type as we want), or report that it’s 
not possible to select coins in such a way that they sum up to S.
"""
import unittest
import sys

def coins(coins, change):
	dp = [sys.maxsize] * (change + 1)	
	dp[0] = 0

	for i in range(1, change + 1):
		for j in coins:
			if j <= i and dp[i-j] + 1 < dp[i]:
				dp[i] = dp[i-j] + 1
	return dp[change]




class Test(unittest.TestCase):
	data_coins = [1, 3, 5]
	data = [
		(0, 0),
		(1, 1),
		(2, 2),
		(3, 1),
		(5, 1),
		(10, 2),
		(11, 3),
		(5600, 1120)
	]

	def test_coins(self):
		for (change, expected) in self.data:			
			self.assertEqual(coins(self.data_coins, change), expected)


unittest.main()