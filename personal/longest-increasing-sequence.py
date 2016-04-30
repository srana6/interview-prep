
def LIS(arr):
	n = len(arr)
	memo = [1] * n

	for i in range(1, n):
		for j in range(i):
			if arr[j] <= arr[i]:
				memo[i] = max(memo[i], 1 + memo[j])
	
	print (memo)

arr = [5, 3, 4, 8, 6, 1]
LIS(arr)


# 3, 4, 6, 7