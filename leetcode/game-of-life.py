class Solution(object):
    
    moves = 8
    boundsX = [-1, 0,  1, 1, 1, 0, -1, -1]
    boundsY = [-1, -1,-1, 0, 1, 1,  1,  0]
    
    def bounds(self, n, m, i, j):
        return  i >= 0 and i < n and j >= 0 and j < m
    
    def getNeighbours(self, grid, n, m, i, j):
        neighbours = 0
        for x in range(self.moves):
            newI = i + self.boundsY[x]
            newJ = j + self.boundsX[x]
            
            if self.bounds(n, m, newI, newJ) and (grid[newI][newJ] == 1 or grid[newI][newJ] == 3):
                neighbours += 1
        return neighbours
        
    def isAlive(self, grid, n, m, i, j):
        neighbours = self.getNeighbours(grid, n, m, i, j)
                
        if grid[i][j] == 0:
            if neighbours == 3:
                return True        
        else:
            if neighbours == 2 or neighbours == 3:
                return True        
        return False
            
    
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return
        n = len(board)
        m = len(board[0])
                
        for i in range(n):
            for j in range(m):
                if self.isAlive(board, n, m, i, j):
                    if board[i][j]:
                        board[i][j] = 3
                    else:
                        board[i][j] = 4
                else:
                    board[i][j] = 2
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 3:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
        
    

grid = [[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]

Solution().gameOfLife(grid)

print (grid)