"""
.258
Given a non-negative integer num, repeatedly add all 
its digits until the result has only one digit.

For example:
Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. 
Since 2 has only one digit, return it.
"""

class Solution(object):
    def _addDigits2(self, num):
        num_str = str(num)
        count = 99

        while len(str(count)) > 1:
            count = 0
            for i in range(len(num_str)):
                count += int(num_str[i])
            num_str = str(count)

        return count

    def _addDigits(self, num):
        
        while num >= 10:
            count = 0
            while num > 0:
                count += num % 10
                num = int(num / 10)         
            num = count

        return num 


    def addDigits(self, num):
        if num < 10:
            return num
        else:
            return 1 + ((num - 1) % 9)


print ( Solution().addDigits(65536) )