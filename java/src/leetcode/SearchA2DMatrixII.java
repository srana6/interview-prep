package leetcode;

public class SearchA2DMatrixII {
	
	public static boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0)
        	return false;
        
        int m = matrix.length;
        int n = matrix[0].length;
        int row = 0;
        int col = n - 1;
        
        while(col >= 0 && row < m){
        	int value = matrix[row][col];
        	System.out.println(value);
        	
        	if (value == target){
        		return true;
        	}
        	else if(value < target){
        		row++;        		
        	}
        	else{
        		col--;
        	}        	
        }
		return false;
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
