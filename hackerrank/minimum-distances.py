"""

Consider an array of  integers, . The distance between two indices,  and , is denoted by .

Given , find the minimum  such that  and . In other words, find the minimum distance between any pair of equal elements in the array. If no such value exists, print .

Note:  denotes the absolute value of .

Input Format

The first line contains an integer, , denoting the size of array . 
The second line contains  space-separated integers describing the respective elements in array .

Constraints

Output Format

Print a single integer denoting the minimum  in ; if no such value exists, print .

Sample Input

6
7 1 3 4 1 7
Sample Output

3
Explanation 
Here, we have two options:

 and  are both , so .
 and  are both , so .
The answer is . min(3, 5) = 3

"""

from collections import defaultdict

INF = float("inf")

def get_min(indexes):
	m = len(indexes)
	minimum = INF

	for i in range(m):
		for j in range(i + 1, m):
			distance = indexes[j] - indexes[i]
			minimum = min(minimum, distance)

	return minimum

def minimum_distance(A, n):
	
    values = defaultdict(list)
    minimum = INF
    
    for i in range(n):
        elem = A[i]
        values[elem].append(i)

    for value, indexes in values.items():
    	if len(indexes) > 1:
    		minimum = min(minimum, get_min(indexes))
    
    return minimum if minimum != INF else -1

n = 6
A = [7, 1, 3, 4, 1, 7]
minimum_distance(A, n)