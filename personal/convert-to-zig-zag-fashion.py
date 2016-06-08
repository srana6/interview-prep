"""
Convert array into Zig-Zag fashion
Given an array of distinct elements, rearrange the elements of array in zig-zag fashion in O(n) time. The converted array should be in form a < b > c < d > e < f.

Example: 
Input:  arr[] = {4, 3, 7, 8, 6, 2, 1}
Output: arr[] = {3, 7, 4, 8, 2, 6, 1}

Input:  arr[] =  {1, 4, 3, 2}
Output: arr[] =  {1, 4, 2, 3}

Analysis:
	Runtime O(n)

	In order to solve this problem linearly, we can control the zigzag property with a flag, each iteration
	the flag is exchanged to denote  < or > .
	In this case,  

	order:
		True   <
		False  >

"""


def zigzag(arr):
	if not arr: return []
	n = len(arr)
	order = True

	for i in range(n - 1):
		# check if the order is correct, if not swap
		if not check_order(arr[i], arr[i + 1], order):				
			arr[i], arr[i + 1] = arr[i + 1], arr[i]			
		order = not order

	return arr


def check_order(a, b, order):
	if order:
		return a < b
	else:
		return a > b


arr = [4, 3, 7, 8, 6, 2, 1]
res = zigzag(arr)
print (res)
