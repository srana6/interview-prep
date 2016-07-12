class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, numbers):
        if not numbers: return -1        
        n = len(numbers)
        jumps = 0

        cur_end = 0
        cur_farthest = 0

        for i in range(n - 1):
            cur_farthest = max(cur_farthest, i + numbers[i])

            if i == cur_end:
                jumps += 1
                cur_end = cur_farthest

        if cur_end >= n - 1:
            return jumps

        return -1 



A = [2,1,1,0,4]

#      [0,  ,  ,  ,  ,  ]

sol = Solution().jump(A) 
print (sol)


"""

a b c d e

a
    b   c

b
    c   d   e

c
    d

d
    e

"""