package interviewbit.atoi;

public class Solution {
	
	public static int char_digit(Character digit){
        switch(digit){
            case '0': return 0;
            case '1': return 1;
            case '2': return 2;
            case '3': return 3;
            case '4': return 4;
            case '5': return 5;
            case '6': return 6;
            case '7': return 7;
            case '8': return 8;
            case '9': return 9;
        }
        return -1;
    }
    
	public static int atoi(final String original) {
	    if (original == null) return 0;
        
        String string = original.trim();
        int size = string.length();
        
        if (size == 0) return 0;
        
        int number = 0;
        int sign = 1;
        
        if (string.charAt(0) == '-' || string.charAt(0) == '+'){
            if (string.charAt(0) == '-')
                sign = -1;
            
            string = string.substring(1, size);
            size --;
        }
        
        
        int j = 0;
        while (j < size && string.charAt(j) >= '0' && string.charAt(j) <= '9'){
            j ++;
        }
        
        
        for (int i = j - 1; i >= 0; i--){
            int digit = char_digit(string.charAt(i));
            int exponent = j - i - 1;
            int extra = (int) (Math.pow(10, exponent) * digit);
            
            if(number + extra < 0){
            	if (sign == 1)
                    return Integer.MAX_VALUE;
                    
                else if(sign == -1)
                    return Integer.MIN_VALUE;
            }
            
            number += extra;
        }
        return number * sign;
	}
	
	
	public static void main(String[] args) {
		System.out.println(  atoi("1111111144024E11 G24  378556582G0467E    6 613  1 2173 9829 5K5H099 2Q  458890732 94  0 ")  ); 
	}
}
