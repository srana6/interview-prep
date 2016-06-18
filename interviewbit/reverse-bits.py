"""


Reverse bits of an 32 bit unsigned integer

Example 1:

x = 0,

          00000000000000000000000000000000  
=>        00000000000000000000000000000000
return 0

Example 2:

x = 3,

          00000000000000000000000000000011 
=>        11000000000000000000000000000000
return 3221225472

"""


class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, num):        
        result = 0
        mask = 1

        for i in range(32):
            # increases result bin size
            result = result << 1

            # if least significant bit is On in num, turn it On in result
            if num & mask == 1:
                result |= mask

            # remove least significant bit from num
            num = num >> 1
        return result

num = 3
sol = Solution().reverse(num)
print (sol,   bin(sol))

