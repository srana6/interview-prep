"""

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).

You are given a target value to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Input : [4 5 6 7 0 1 2] and target = 4
Output : 0

NOTE : Think about the case when there are duplicates. 
Does your current solution work? How does the time complexity change?*

"""


class Solution:
    def findPivot(self, numbers):
        start = 0
        end = len(numbers) - 1
        
        while start < end:
            index = (start + end) // 2
            mid = numbers[index]
            
            if mid > numbers[end]:
                start = index + 1

            elif mid < numbers[end] and numbers[index - 1] < numbers[end]:
                end = index - 1

            else:
                return index
        return end

    def binary_search(self, numbers, start, end, target):        
        while start <= end:
            idx = (start + end) // 2
            val = numbers[idx]

            if val == target:
                return idx

            elif val < target:
                start = idx + 1

            else:
                end = idx - 1

        return -1
        
    
    def search(self, numbers, target):
        if not numbers: return -1
        size = len(numbers)
        
        pivot = self.findPivot(numbers)
        indices = [(0, pivot), (pivot, size - 1)]

        found = self.binary_search(numbers, 0, pivot, target)
        if found != -1:
            return found
        
        return self.binary_search(numbers, pivot, size - 1, target)
            
                
arr = [1, 7, 67, 133, 178]
pivot = Solution().findPivot(arr)
print (pivot)

sol = Solution().search(arr, 1)
print (sol)
