"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
"""



class Solution(object):
    def convertToTitle(self, n):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        size = len(letters)
        title = []

        while n > 0:            
            title.append(letters[n % size - 1])    
            n = (n - 1) // size

        title = reversed(title)
        return ''.join(title)


sol = Solution()
print ( sol.convertToTitle(999) )
        
