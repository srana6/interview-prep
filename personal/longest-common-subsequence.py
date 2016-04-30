"""
 Given two sequences, find the length of longest subsequence present in both of them. 
 Both the strings are of uppercase.

Input:
First line contains no of test cases T, for every test case 2 integers are input and then 
in next two lines, two strings of sizes equal to 2 integers respectively are given as a input.


Output:
Each new line printing length of longest subsequence.


Constraints:
1<=T<=30
1<=size(str1),size(str2)<=100


Example:
Input:
1
6 6
ABCDGH
AEDFHR

Output:
3

Explaination :
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.

"""

# Recursion tree takes 2^n  exponential time
def LCS(A, B, n = None, m = None):
	if not A or not B: return 0

	if n is None: n = len(A)
	if m is None: m = len(B)

	if n == 0 or m == 0:
		return 0

	# values are equal, get the highest LCS and add 1
	elif A[n - 1] == B[m - 1]:
		return 1 + LCS(A, B, n - 1, m - 1)

	else:
		# recurse to get the max when the values are different
		return max(LCS(A, B, n - 1, m), LCS(A, B, n, m - 1))



def longest_common_subsequence(X, Y):
	if not X or not Y: return 0

	# length of the strings
	n = len(X)
	m = len(Y)

	# store dp values
	table = [[None] * (m + 1) for i in range(n + 1)]
	
	for i in range(n + 1):
		for j in range(m + 1):
			if i == 0 or j == 0:
				table[i][j] = 0

			elif X[i - 1] == Y[j - 1]:
				table[i][j] = 1 + table[i - 1][j - 1]

			else:
				table[i][j] = max(table[i - 1][j], table[i][j - 1])


	for row in table:
		print (row)

	return table[n][m]







memo = {}

def LCS_memo(A, B, i = None, j = None):
	if not A or not B: return 0
	if i is None: i = len(A)
	if j is None: j = len(B)

	if (i, j) not in memo:

		if i == 0 or j == 0:
			memo[(i, j)] = 0

		else:			
			if A[i - 1] == B[j - 1]:
				memo[(i, j)] = LCS_memo(A, B, i - 1, j - 1) + 1
			else:
				memo[(i, j)] = max(LCS_memo(A, B, i - 1, j), LCS_memo(A, B, i, j - 1))

				
	return memo[(i, j)]





X = "ABCDGH"
Y = "ADH"

X = "AGGTAB"
Y = "GXTXAYB"

sol = longest_common_subsequence(X, Y)
sol = LCS_memo(X, Y)


#sol = LCS(X, Y)
print (sol)