"""
Dynamic Programming

Distinct SubsequencesBookmark

Given two sequences S, T, count number of unique ways in sequence S, to form a subsequence that is identical to the sequence T.

Subsequence : A subsequence of a string is a new string which is formed from the original string by deleting some 
(can be none ) of the characters without disturbing the relative positions of the remaining characters. 
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not). 

Example :
 S = "rabbbit" T = "rabbit" 

Return 3. And the formations as follows:

S1= "ra_bbit" 
S2= "rab_bit" 
S3="rabb_it"
"_" marks the removed character.

"""

class Solution:
	def numDistinct(self, string, target):
		size_string = len(string)
		size_target = len(target)
		memo = [[0] * (size_string + 1) for _ in range(size_target + 1)]

		for i in range(size_string + 1):
			memo[0][i] = 1

		for i in range(1, size_target + 1):
			for j in range(1, size_string + 1):

				# Calculated before without new char
				memo[i][j] = memo[i][j - 1]

				# Calculated previous step
				if target[i - 1] == string[j - 1]:
					memo[i][j] += memo[i - 1][j - 1]

		return memo[size_target][size_string]


resp = Solution().numDistinct("ABTFCACDD", "ABCCD")
print (resp)
