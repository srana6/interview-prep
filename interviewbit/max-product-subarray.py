class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, numbers):
        if not numbers: return 0
        size = len(numbers)
        _max = [0] * size
        _min = [0] * size

        result = numbers[0]
        _max[0], _min[0] = result, result

        for i in range(1, size):
            
            if numbers[i] > 0:
                _max[i] = max(numbers[i], _max[i - 1] * numbers[i])
                _min[i] = min(numbers[i], _min[i - 1] * numbers[i])

            else:
                _max[i] = max(numbers[i], _min[i - 1] * numbers[i])
                _min[i] = min(numbers[i], _max[i - 1] * numbers[i]) 

            result = max(result, _max[i])

        return result


numbers = [3, 10, -2, 1, -3, -20, -10, -5]
Solution().maxProduct(numbers)