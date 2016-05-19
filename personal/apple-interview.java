
Q. You have two large 1GB plain text files stored in two computers connected by a slow connection. Most of the files is the same or they could be the same, how would you quickly determine if the files are the same and if they are different where are they different?
A.

1gb  -   1gb


  
a b   > c < d       e f g z
  
a b   > x < d       e f g z

  
  
  

/*Q. Could you code binary search on a sorted array?

int binarySearch(int[] array, int value)

returns 1 if found
       -1 if not found
A.

*/

import java.io.*;
import java.util.*;

/*
 * To execute Java, please define "static void main" on a class
 * named Solution.
 *
 * If you need more classes, simply define them inline.
 */

//  0

//  1 2 30  4   5 6 7    

/*
class Solution {
  public static int binarySearch(int[] arr, int element){
    int start = 0;
    int end = arr.length - 1;
    
    while (start <= end){
      int midIndex = (start + end) / 2;
      int midValue = arr[midIndex];
            
      if (midValue == element){
        return 1;
      }
      else if(element < midValue){
        end = midIndex - 1;
      }
      else {
        start = midIndex + 1;
      }
      
    }    
    return -1;
  }
  
  
  
  public static void main(String[] args) {
    ArrayList<String> strings = new ArrayList<String>();
    strings.add("Hello, World!");
    strings.add("Welcome to CoderPad.");
    strings.add("This pad is running Java 8.");

    for (String string : strings) {
      System.out.println(string);
    }
    
    
    int[] arr = {1, 2, 3, 4, 5, 6, 7};
    int result = binarySearch(arr, 1);    
    System.out.println(result);
    
  }
}
*/


/*Q. Design a data structure that does the following operations in constant time
  - Push
  - Pop
  - Find Min [doesn't change state]
A.

Stack               
Push (1)
Pop (1)

512 6 1024  6 1
1
              
stack ->   512  6 1024 6 1  
minStack ->  512 6 6 1

(A, 10)
(B, 20)
              
              
hello
hello -> 10, 20
              
public class KeyValue {
  private String key;
  private int value;
}
              
public class HashTable {
  
  private ArrayList<String> keys;
  private ArrayList<LinkedList<KeyValue>> values;
  
  public HashTable(){
    this.keys = new ArrayList<>();
    
  }
  
  
  
  
}
              








/*import java.io.*;
import java.util.*;

/*
 * To execute Java, please define "static void main" on a class
 * named Solution.
 *
 * If you need more classes, simply define them inline.
 */
/*
class Solution {
  public static void main(String[] args) {
    ArrayList<String> strings = new ArrayList<String>();
    strings.add("Hello, World!");
    strings.add("Welcome to CoderPad.");
    strings.add("This pad is running Java 8.");

    for (String string : strings) {
      System.out.println(string);
    }
  }
}*/
