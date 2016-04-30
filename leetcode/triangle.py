class Solution(object):
    
    def getValue(self, triangle, row, col):
        if row >= 0 and row < len(triangle) and col >= 0 and col < len(triangle[row]):
            return triangle[row][col]
        return None
    
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Triangle empty
        if not triangle: return 0
        
        N = len(triangle)
        MAX = float("inf")
        
        # Memoize minimum path for each row
        memo = []
        for row in triangle:
            memo.append([MAX] * len(row))
        memo[0][0] = triangle[0][0]
        
        for row in range(N):
            for col in range(len(triangle[row])):
                if self.getValue(memo, row - 1, col - 1) is not None:
                    memo[row][col] = min(memo[row][col], self.getValue(memo, row - 1, col - 1) + triangle[row][col] )
                                     
                if self.getValue(memo, row - 1, col) is not None:
                    memo[row][col] = min(memo[row][col], self.getValue(memo, row - 1, col) + triangle[row][col] )
                                    
        
        result = MAX
        for j in range(len(memo[N - 1])):
            result = min(result, memo[N-1][j])
            
        return result
            
        