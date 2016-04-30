"""
On a positive integer, you can perform any one of the following 3 steps. 
1.) Subtract 1 from it. ( n = n - 1 )  , 
2.) If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2  )  , 
3.) If its divisible by 3, divide by 3. ( if n % 3 == 0 , then n = n / 3  ). 

Now the question is, given a positive integer n, 
find the minimum number of steps that takes n to 1
"""
import sys

def msteps(n):
	dp = [-1 for i in range(n + 1)]
	dp[1] = 0

	for i in range(2, n + 1):
		dp[i] = 1 + dp[i - 1]
		if i % 2 == 0: dp[i] = min(dp[i], int(i / 2))
		if i % 3 == 0: dp[i] = min(dp[i], int(i / 3))
	
	return dp[n]

print (msteps(100))