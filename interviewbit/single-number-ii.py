"""
Given an array of integers, every element appears thrice except for one which occurs once.

Find that element which does not appear thrice.

Note: Your algorithm should have a linear runtime complexity.

Could you implement it without using extra memory?

Example :

Input : [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
Output : 4

"""

class Solution:    

    def singleNumber(self, nums):
        size = 32
        arr = [0] * size

        # for each number,  count its bits
        for num in nums:

            # aggregate in an array the bits of the curr number
            i = 31
            while num:
                bit = num & 1
                if bit == 1:
                    arr[i] += 1

                num = num >> 1
                i -= 1 

        # after having counted, remove the counts that form multiples of 3 bits, which relate to
        # all duplicate numbers
        
        for i in range(size):
            arr[i] = str(arr[i] % 3)

        return int("".join(arr), 2)



arr = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]

sol = Solution().singleNumber(arr)
print ('sol', sol)

print (bin(4)[2:])

# If X has 1 in that position, we will have (3x+1) number of 1s in that position.
# If X has 0 in that position, we will have (3x+1) number of 0s in that position.