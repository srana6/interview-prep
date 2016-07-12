package hackerrank;

import java.util.Scanner;

public class LarryArray {

	public static boolean isSorted(int[] arr){
        for(int i = 0; i < arr.length - 1; i++){
            if (arr[i] > arr[i + 1])
                return false;
        } 
        return true;
    }
    
    public static boolean sorted(int a, int b, int c){
        return (a < b && a < c);
    }
    
    public static boolean solution(int[] arr){
        if (arr == null || arr.length == 0) return false;
        
        boolean changes = true;
        while (changes){            
            changes = false;            
            for (int i = 0; i < arr.length - 2; i++){
                int a = arr[i];
                int b = arr[i + 1];
                int c = arr[i + 2];
                
                if (sorted(b, c, a)){
                    arr[i] = b;
                    arr[i + 1] = c;
                    arr[i + 2] = a;
                    
                    changes = true;
                }
                else if (sorted(c, a, b)){
                    arr[i] = c;
                    arr[i + 1] = a;
                    arr[i + 2] = b;
                    changes = true;
                }
            }            
        }
            
        return isSorted(arr);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        while (tc > 0){
            int n = sc.nextInt();
            int[] arr = new int[n];
            
            for (int i = 0; i < n; i++){
                arr[i] = sc.nextInt();
            }
            
            if (solution(arr)){
                System.out.println("YES");
            }
            else{
                System.out.println("NO");
            }
            tc --;
        }
    }

}
