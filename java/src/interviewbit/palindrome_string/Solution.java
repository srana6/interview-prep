package interviewbit.palindrome_string;

/*

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example:

"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem


 */	
public class Solution {
	
	public static boolean isAlphanumeric(char a){
		return (a >= 'a' && a <= 'z') ||( a >= '0' && a <= '9') || (a >= 'A' && a <= 'Z');
	}

	public static int isPalindrome(String string) {
		if (string == null || string.length() == 0)
			return 0;
		
		int start = 0;
		int end = string.length() - 1;
		
		while (start <= end){
			char left = string.charAt(start);
			char right = string.charAt(end);
			
			if (!isAlphanumeric(left))
				start ++;
			
			else if (!isAlphanumeric(right))
				end --;
			
			else {
				
				if (Character.toLowerCase(left) == Character.toLowerCase(right)){
					start ++;
					end --;
				}
				else{
					return 0;
				}
			}
		}
		
		return 1;		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str = "1a2";
		System.out.println(isPalindrome(str));

	}

}
