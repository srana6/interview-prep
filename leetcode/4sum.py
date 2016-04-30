"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
"""



class Solution2(object):
    def ksum(self, nums, target):        
        size = len(nums)
        i = 0
        j = size - 1
        aux = []
        while i < j:
            if nums[i] + nums[j] == target:
                aux.append( (nums[i], nums[j]) )
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        return aux

    def fourSum(self, nums, target):
        nums.sort()
        size = len(nums)
        result = set([])
        pairs = None

        for i in range(size - 2):
            for j in range(i + 1, size):                
                pairs = self.ksum(nums[j + 1:], target - (nums[i] + nums[j]), )
                if pairs:
                    for pair in pairs:
                        result.add( tuple([nums[i], nums[j], pair[0], pair[1]]) )
        return ([list(i) for i in result])





class Solution(object):

    # Almost Brute Force
    #  Calculating all permutations of 4 groups. Keeping in stack
    def ksum(self, nums, target, result, aux, N, total, pos):
        size = len(aux)            
        if size < N:
            for i in range(pos, len(nums)):
                total += nums[i]
                aux.append(nums[i])
                self.ksum(nums, target, result, aux, N, total, i + 1)
                aux.pop()
                total -= nums[i]
        else:
            if total == target:
                result.add(tuple(aux))
    def fourSum2(self, nums, target):
        nums.sort()        
        result = set([])
        self.ksum(nums, target, result, [], 4, 0, 0)
        return ([list(i) for i in result])

test = [-3,-2,-1,0,0,1,2,3]

sol = Solution2()
rs = sol.fourSum(test, 0)


for i in rs:
    print(i)
