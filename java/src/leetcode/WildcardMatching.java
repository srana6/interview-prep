package leetcode;

public class WildcardMatching {
	public boolean isMatch(String string, String pattern) {	
        boolean[][] memo = new boolean[pattern.length() + 1][string.length() + 1];
        memo[0][0] = true;
        
        // Every * from beginning is true
        for (int i = 1; i <= pattern.length(); i++){
            if(pattern.charAt(i - 1) != '*')
                break;
            else
                memo[i][0] = true;
        }
                
        for (int i = 1; i <= pattern.length(); i++){
            for(int j = 1; j <= string.length(); j++){
                
            	// If match or '?' any character matches
                if(pattern.charAt(i - 1) == string.charAt(j - 1) || pattern.charAt(i - 1) == '?')
                    memo[i][j] = memo[i - 1][j - 1];
                
                // If something valid before, this is valid
                else if(pattern.charAt(i - 1) == '*')
                    memo[i][j] = memo[i- 1][j] || memo[i][j - 1];
                    
                // Not valid
                else
                    memo[i][j] = false;
            }
        }
        
        return memo[pattern.length()][string.length()];
    }		
}
