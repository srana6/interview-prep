"""
ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".



-----------
Solution uses an array of rows to store characters that belong to each of them
O(n)
It adds linearly the element to the correspondent row[i]  by moving up or down across the rows

"""

from itertools import chain

class Solution(object):
    def convert(self, string, numRows):
        steps = (numRows == 1) - 1
        rows = [[] for _ in range(numRows)]
        
        print (steps)

        idx = 0
        for elem in string:
            rows[idx].append(elem)

            # change of direction between rows array
            if idx == 0 or idx == numRows - 1:
                steps = -steps

            idx += steps


        result = list(chain.from_iterable(rows))
        print (result)
        print (*rows)   # * performs an unpacking of the list
        print (rows)

        return "".join(result)




string = "PAYPALISHIRING"

Solution().convert(string, 3)
        
        
