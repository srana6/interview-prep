"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.
"""

class Solution(object):
    def digitNum(self, digit):
        if digit == '0':
            return 0
        elif digit == '1':
            return 1
        elif digit == '2':
            return 2
        elif digit == '3':
            return 3
        elif digit == '4':
            return 4
        elif digit == '5':
            return 5
        elif digit == '6':
            return 6
        elif digit == '7':
            return 7
        elif digit == '8':
            return 8
        elif digit == '9':
            return 9
        return None

    def myAtoi(self, string):
        strNum = string.strip()
        size = 0
        sign = 1
        pos = 0
        num = 0
        if strNum:
            if self.digitNum(strNum[pos]) is None:
                if strNum[pos] == '-':
                    sign = -1
                    pos = 1
                elif  strNum[pos] == '+':
                    pos = 1
                else:
                    return 0

            for i in range(pos, len(strNum)):
                if self.digitNum(strNum[i]) is not None:
                    size += 1
                else:
                    break
            
            for i in reversed(range(size)):
                digit = self.digitNum(strNum[pos])
                exp = pow(10, i)
                num += digit * exp
                pos += 1

            num = num * sign

            if sign == 1 and num > 2147483647:
                return 2147483647
            elif sign == -1 and num < -2147483648:
                return -2147483648

            return num
        return 0


sol = Solution()
print (sol.myAtoi("2147483648"))