# Analysis
# Use a cache to store the distances of the minimum path sums
# Check for the position up and left for each of the fields
# -> O(m*n)
# return cache[m - 1][n - 1]



class Solution(object):
    MAX = float("inf")
    
    # Check boundaries and get cache value
    def getFieldValue(self, table, row, col):
        if row >= 0 and row < len(table) and col >=0 and col < len(table[row]):
            return table[row][col]
        return self.MAX
    
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # If grid empty, don't do anything
        if not grid or not grid[0]: return 0
        

        # Help variables
        M = len(grid)
        N = len(grid[0])
        lastRow = M - 1
        lastCol = N - 1
        
        # Initialize cache for memoization, remember the best min sum
        cache = [[self.MAX] * N for i in range(M)]
        cache[0][0] = 0


        # Iterate over matrix and cache min sum
        for row in range(M):
            for col in range(N):
                cache[row][col] = grid[row][col] + min( cache[row][col], 
                                                        self.getFieldValue(cache, row - 1, col),
                                                        self.getFieldValue(cache, row, col - 1) )
        return cache[lastRow][lastCol]
                
        
        
Solution().minPathSum([[0]])