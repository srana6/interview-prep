"""

You are given a set of coins S. In how many ways can you make sum N assuming you have infinite amount of each coin in the set.

Note : Coins in set S will be unique. Expected space complexity of this problem is O(N).

Example :

Input : 
	S = [1, 2, 3] 
	N = 4

Return : 4

Explanation : The 4 possible ways are
{1, 1, 1, 1}
{1, 1, 2}
{2, 2}
{1, 3}	

Note that the answer can overflow. So, give us the answer % 1000007

"""

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer

	overflow = 1000007

	def coinchange2(self, coins, total):
		ncoins = len(coins)
		memo = [0] * (total + 1)
		memo[0] = 1

		for coin in coins:
			for money in range(1,total + 1):
				remaining = money - coin

				if remaining >= 0:
					memo[money] += memo[remaining]
		
		return memo[total] % self.overflow


S = [1, 2, 3] 
N = 4 

resp = Solution().coinchange2(S, N)

print (resp)                                      



