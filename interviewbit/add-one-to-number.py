"""

Add One To Number

Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.

 NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer.
For example, for this problem, following are some good questions to ask :
Q : Can the input have 0’s before the most significant digit. Or in other words, is 0 1 2 3 a valid input?
A : For the purpose of this question, YES
Q : Can the output have 0’s before the most significant digit? Or in other words, is 0 1 2 4 a valid output?
A : For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.



# arr empty
# arr smaller at end
# arr leading zeroes
#  [0, 0, 1, 9, 9]
          2  0   0

A : [ 9, 9, 9, 9, 9 ]
    

"""



class Solution:

    # solution doing reverse
    def plusOne(self, arr):
        if not arr: return [1]
        size = len(arr)        
        result = []
        carry = 1

        for i in reversed(range(size)):
            _sum = arr[i] + carry     
            result.append(_sum % 10)
            carry = _sum // 10

        while carry:
            result.append(carry % 10)
            carry = carry // 10

        while result[-1] == 0 and len(result) > 1:
            result.pop()
        
        return result[::-1]


    # solution without reverse
    def plusOne2(self, arr):
        if not arr: return [1]
        size = len(arr)

        carry = 1
        end = size - 1
        while end >= 0 and carry > 0:
            arr[end] += carry
            carry = 0

            
            if arr[end] > 9: 
                carry = 1
            arr[end] = arr[end] % 10

            end -= 1


        if carry != 0:
            arr = [1] + arr            

        elif end != 0:
            zeroes = self.leftZeroes(arr, end + 1)
            if zeroes > 0:
                arr = arr[zeroes:]

        return arr





    def leftZeroes(self, arr, end = None):
        if not arr: return 0        
        if not end: end = len(arr)
        idx = 0
        while idx < end and arr[idx] == 0:
            idx += 1

        return idx





A = [ 9, 9, 9, 9, 9, 9 ]
sol = Solution().plusOne(A)
print(sol)