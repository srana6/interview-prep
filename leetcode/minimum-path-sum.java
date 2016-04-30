public class minimum-path-sum {
    int[][] memo;
    
    public int minPathSum(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;
        
        memo = new int[row][col];
        for(int i=0; i< row; i++){
            for(int j=0; j< col; j++){
                memo[i][j] = Integer.MAX_VALUE;
            }
        }
        memo[0][0] = 0;
       
        return RecurseSum(grid, row - 1, col - 1);
        
    }

    public int RecurseSum(int[][] arr, int i, int j){
        if (i < 0 || j < 0)
            return Integer.MAX_VALUE;

        else if(i == 0 && j == 0)
            return arr[0][0];

        else
            return arr[i][j] + Math.min(
                                RecurseSum(arr, i - 1, j), 
                                RecurseSum(arr, i, j - 1));        
    }

    public static void main(){

    }
}
