package hackerrank;

import java.util.Scanner;

public class NewYearChaos {

	public static int solution(int[] arr){
        if (arr == null || arr.length == 0) return -1;
        
        int[] bribes = new int[arr.length];
        int moves = 0;        
        boolean valid = true;
        
        while (valid){
            valid = false;
            
            for (int i = 0; i < arr.length - 1; i++){
                int idx = arr[i] - 1;
                
                if(arr[i] > arr[i + 1]){                    
                    int aux = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = aux;
                    
                    moves ++;
                    valid = true;
                    
                    bribes[idx] ++;
                    if (bribes[idx] > 2)
                        return -1;
                }
            } 
        }
          
        return moves;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        for(int a0 = 0; a0 < T; a0++){
            int n = in.nextInt();
            int q[] = new int[n];
                        
            for(int q_i=0; q_i < n; q_i++){
                q[q_i] = in.nextInt();
            }
            
            int moves = solution(q);
            
            if (moves == -1){
                System.out.println("Too chaotic");
            }
            else{
                System.out.println(moves);
            }
                
        }
    }

}
