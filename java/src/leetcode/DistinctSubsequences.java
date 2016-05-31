package leetcode;

import java.util.Arrays;

public class DistinctSubsequences {
	public static int _numDistinct(String S, String T){		
		int size_T = T.length();
		int size_S = S.length();
		int[][] memo = new int[size_T + 1][size_S + 1];
		Arrays.fill(memo[0], 1);
		
		for (int i = 1; i <= size_T; i++){
			for (int j = 1; j <= size_S; j++){
				memo[i][j] = memo[i][j - 1];
				
				if(T.charAt(i - 1) == S.charAt(j - 1)){
					memo[i][j] += memo[i - 1][j - 1];
				}
			}
		}
		
		for (int[] row : memo){
	    	System.out.println(Arrays.toString(row));
	    }
		
		return memo[size_T][size_S];
	}	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s1 = "ABTFCACDD";
		String s2 = "ABCCD";
		
		int result = _numDistinct(s1, s2);
		System.out.println(result);
	}

}
