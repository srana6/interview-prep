package hackerrank;

import java.util.Arrays;
import java.util.Scanner;

public class Java1DArray {

	public static boolean solution(int[] numbers, int m, int pos){
        if (pos < 0 ) return false;
        if (pos >= numbers.length) return true;
        
        if (numbers[pos] == 0){
            numbers[pos] = 2;
            return solution(numbers, m, pos - 1) || solution(numbers, m, pos + 1) || solution(numbers, m, pos + m);
        }
        
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int test_cases = sc.nextInt();
        
        while (test_cases > 0){
            int n = sc.nextInt();
            int m = sc.nextInt();            
            int[] numbers = new int[n];
            
            for (int i = 0; i < n ; i++){
                numbers[i] = sc.nextInt();
            }
            
            boolean win = solution(numbers, m, 0);
            
            if (win){
                System.out.println("YES");
            }
            else
                System.out.println("NO");
            
            test_cases --;
        }        
    }
}
