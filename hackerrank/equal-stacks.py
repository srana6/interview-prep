"""
You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they're all the same height, then print the height. The removals must be performed in in such a way as to maximize the height.

Note: An empty stack is still a stack.

Input Format

The first line contains three space-separated integers, , , and , describing the respective number of cylinders in stacks , , and . The subsequent lines describe the respective heights of each cylinder in a stack from top to bottom:

The second line contains  space-separated integers describing the cylinder heights in stack .
The third line contains  space-separated integers describing the cylinder heights in stack .
The fourth line contains  space-separated integers describing the cylinder heights in stack .
Constraints

Output Format

Print a single integer denoting the maximum height at which all stacks will be of equal height.

Sample Input

5 3 4
3 2 1 1 1
4 3 2
1 1 4 1
Sample Output

5
"""

#!/bin/python3

class Solution(object):
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def balanced_stacks(self):
        if not self.A or not self.B or not self.C: return 0
        h1, h2, h3, = sum(self.A), sum(self.B), sum(self.C)
        maximum = max(h1, h2, h3)
        a, b, c = -1, -1, -1

        while h1 != h2 or h2 != h3:
            if h1 == maximum:
                a += 1
                h1 -= self.A[a]

            elif h2 == maximum:
                b += 1
                h2 -= self.B[b]

            else:
                c += 1
                h3 -= self.C[c]

            maximum = max(h1, h2, h3)
        return maximum

def read_stdin():
    import sys
    n1, n2, n3 = list(map(int, input().strip().split(' ')))
    A = list(map(int, input().strip().split(' ')))
    B = list(map(int, input().strip().split(' ')))
    C = list(map(int, input().strip().split(' ')))
    solution = Solution(A, B, C).balanced_stacks()    
    print (solution)

    read_stdin()

    

A = [1, 1, 1, 1, 1, 1, 1]
B = [2]
C = [1]
output = Solution(A, B, C).balanced_stacks()
print (output)