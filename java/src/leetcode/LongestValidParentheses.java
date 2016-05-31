package leetcode;

public class LongestValidParentheses {
	
	public static int longestValidParentheses(String parentheses) {		
	    char[] string = parentheses.toCharArray();
	    int size = string.length;
	    int[] memo = new int[size];
	    int longest = 0;
	    int opened = 0;
	    
	    for(int i = 0; i < size; i++){
	    	if (string[i] == '('){
	    		opened ++;
	    	}
	    	else {
	    		if (opened > 0){
	    			opened --;
	    			memo[i] = 2 + memo[i - 1];
	    			
	    			// Check boundaries first
	    			// Verify if previously there was a solution. Add it up
	    			if (i - memo[i] >= 0 && memo[i - memo[i]] > 0){
	    				memo[i] += memo[i - memo[i]];
	    			}
	    		}
	    		longest = Math.max(longest, memo[i]);	    			
	    	}
	    }	    
	    return longest;
	}
	
	public static void main(String[] args) {
		String parentheses = "((()()((()))()()())))))";
		int result = longestValidParentheses(parentheses);
		
		System.out.println(result);
	}
}
