class Triangle(object):
    
    def get_value(self, triangle, row, col):
        if row >= 0 and row < len(triangle) and col >= 0 and col < len(triangle[row]):
            return triangle[row][col]
        return None

    def minimum_path(self, triangle):
        # Triangle empty
        if not triangle: return 0
        
        MIN = -float("inf")
        size = len(triangle)
        
        # Memoize minimum path for each row        
        memo = []

        # Initialize memo table
        for row in triangle:
            memo.append([MIN] * len(row))
        memo[0][0] = triangle[0][0]
        

        # Calculate path
        for row in range(size):
            for col in range(len(triangle[row])):

                if self.get_value(memo, row - 1, col - 1) is not None:
                    memo[row][col] = max(memo[row][col], self.get_value(memo, row - 1, col - 1) + triangle[row][col] )
                                     
                if self.get_value(memo, row - 1, col) is not None:
                    memo[row][col] = max(memo[row][col], self.get_value(memo, row - 1, col) + triangle[row][col] )
                                    
        
        # Obtain minimum path from memoized table
        result = MIN        
        for j in range(size):
            result = max(result, memo[size - 1][j])
            
        return result



def solve(triangle):
    solution = Triangle().minimum_path(triangle)
    print (solution)


def read_input():
    file = "triangle.txt"

    with open(file, 'r') as f:      
        triangle = []

        for _line in f:
            line = list(map(int, _line.strip().split()))
            triangle.append(line)

        solve(triangle)



if __name__ == '__main__':
    read_input()








