"""
60. Permutation Sequence My Submissions QuestionEditorial Solution
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"

Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

Analysis:
	Brute Force
		Calculate all different permutations for the given 'n'
		and then sort the elements
		Time O(n!)
		Space O(n!)

	We are looking for the k'th permutation.
	This means we don't really need to calculate all of them.
	If we could beforehand know whats the probable permutation then good
	Permutations can be seen as a permutation tree with as many child nodes
	as characters to permute

		                          1 

		1                2                3  ... n

	1 ... n - 1     1... n - 1

"""

def permute(string, start = 0, end = None):
	if end is None: end = len(string) - 1
	if start == end:
		print ("".join(string))
	else:
		for i in range(start, end + 1):
			string[start], string[i] = string[i], string[start]
			permute(string, start + 1, end)
			string[start], string[i] = string[i], string[start]

class Solution(object):
	def getPermutation(self, n, k):
		array = [str(i) for i in range (1, n + 1)]
		print (array)

		"""
		:type n: int
		:type k: int
		:rtype: str
		"""

Solution().getPermutation(3, 4)
sol = permute(["1", "2", "3"])
print (sol)