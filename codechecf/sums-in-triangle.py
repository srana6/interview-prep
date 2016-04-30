"""
All submissions for this problem are available.

Let's consider a triangle of numbers in which a number appears in the first line, 
two numbers appear in the second line, three in the third line, etc. Develop a 
program which will compute the largest of the sums of numbers that appear on the 
paths starting from the top towards the base, so that:
on each path the next number is located on the row below, more precisely either 
directly below or below and one place to the right;
the number of rows is strictly positive, but less than 100
all numbers are positive integers between O and 99.
Input

In the first line integer n - the number of test cases (equal to about 1000). 
Then n test cases follow. Each test case starts with the number of lines which is followed by their content.
Output

For each test case write the determined value in a separate line.
Example

Input:
2
3
1
2 1
1 2 3
4 
1 
1 2 
4 1 2
2 3 1 1 

Output:
5
9

"""

def sums_in_triangule(rows, row):
	while row > 0:
		for i in range(row - 1):
			rows[row - 2][i] += max(rows[row - 1][i], rows[row - 1][i + 1]) 
		row -= 1
	return rows[0][0]

def read_by_stdin():
	t = int(input())
	for test_case in range(t):
		n = int(input())
		rows = []

		for l in range(n):
			line = [int(x) for x in input().split()]
			rows.append(line)

		sums_in_triangule(rows, n)

triangle_1 = [[1], [2, 1], [1, 2, 3]]
triangle_2 = [[1], [1, 2], [4, 1, 2], [2, 3, 1, 1]]
triangle_3 = [[5], [1, 7], [6, 3, 4]]

print (sums_in_triangule(triangle_3, 3))