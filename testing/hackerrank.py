import sys

N = int(input())
arr = [int(i) for i in input().split()]


lines = int(input())



lines = int(input())
arr = []
total = 0

for i in range(lines):
    elem = int(input())
    arr.append(elem)
    total += elem
    
print (total)




n = int(input())
for i in range(n):
    a, b = input().strip().split(' ')
    print (int(a) + int(b))


"""


import java.io.*;
import java.util.*;

class Solution
{
    public static void main(String [] args) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int t = 0; t < n; t++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            System.out.println(a+b);
        }
    }
}



n = int(raw_input())
for i in range(0,n):
    a, b = raw_input().split()
    print int(a) + int(b)

"""