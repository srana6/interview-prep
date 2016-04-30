"""
On a positive integer, you can perform any one of the following 3 steps. 1.) 
Subtract 1 from it. ( n = n - 1 )  , 
2.) If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2  )  , 
3.) If its divisible by 3, divide by 3. ( if n % 3 == 0 , then n = n / 3  ). 

Now the question is, given a positive integer n, find the minimum number of steps that takes n to 1

1.) For n = 1 , output: 0       
2.) For n = 4 , output: 2  ( 4  / 2 = 2 / 2 = 1 )    
3.) For n = 7 , output: 3  (  7  - 1 = 6 / 3 = 2 / 2 = 1 )

"""


memo = {}
def calculate_minimum_steps(num):
	if num == 1:
		return 0

	if num in memo:
		return memo[num]

	result = 1 + calculate_minimum_steps(num - 1)

	if num % 2 == 0:
		result = min(result, 1 + calculate_minimum_steps(num // 2))

	if num % 3 == 0:
		result = min(result, 1 + calculate_minimum_steps(num // 3))

	memo[num] = result
	return result

def calculate_minimum_steps_dp(num):
	memoization = [0] * (num + 1)	
	memoization[1] = 0

	for i in range(2, num + 1):		
		memoization[i] = 1 + memoization[i - 1]
		if i % 2 == 0:
			memoization[i] = min(memoization[i], 1 + memoization[i // 2])

		if i % 3 == 0:
			memoization[i] = min(memoization[i], 1 + memoization[i // 3])

	return memoization[num]

solution = calculate_minimum_steps_dp(10000000)
print (solution)