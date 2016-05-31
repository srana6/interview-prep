"""
The numbers on a telephone keypad are arranged thus:

1 2 3
4 5 6
7 8 9
  0

Starting from the digit 1, and choosing successive digits as a knight moves in chess, determine how many 
different paths can be formed of length n. There is no need to make a list of the paths, only to count them.

A knight moves two steps either horizontally or vertically followed by one step in the perpendicular direction; 
thus, from the digit 1 on the keypad a knight can move to digits 6 or 8, and from the digit 4 on the keypad a knight 
can move to digits 3, 9 or 0. A path may visit the same digit more than once.

Your task is to write a function that determines the number of paths of length n that a knight can trace on a keyboard 
starting from digit 1. When you are finished, you are welcome to read or run a suggested solution, or to post your 
own solution or discuss the exercise in the comments below.
"""

moves = [[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]

def knight_moves(length, start = 1):
    dp = [[[0 for i in range(length + 1)] for j in range(10)] for k in range(10)]

    for a in range(10):
        for b in moves[a]:
            dp[a][b][1] = 1

    for k in range(2, length + 1):
        for c in range(10): 
            for a in moves[c]:
                for b in moves[a]:
                    dp[a][b][k] = dp[a][b][k] + dp[c][a][k - 1]

    for end in moves[start]:
        if dp[start][end][length] != 0:
            return dp[start][end][length] 

    return 0

sol = knight_moves(100)
print (sol)