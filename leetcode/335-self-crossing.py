"""
Self crossing

You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, 
then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words, 
after each move your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.

"""

class Solution(object):
		
	def isSelfCrossing(self, arr):
		if not arr: return False
		n = len(arr)

		for i in range(3, n):
			if arr[i] >= arr[i - 2] and arr[i - 1] <= arr[i - 3]:
				return True

			elif i >= 4 and arr[i - 1] == arr[i - 3] and arr[i] + arr[i - 4] >= arr[i - 2]:
				return True

			elif i >= 5 and arr[i - 2] >= arr[i - 4] \
						and arr[i] + arr[i - 4] >= arr[i - 2] \
						and arr[i - 1] <= arr[i - 3] \
						and arr[i - 1] + arr[i - 5] >= arr[i - 3]:
				return True
			
		return False
			
