"""
Given two sorted arrays, find the number of elements in common. 
The arrays are the same length and each has all distinct elements.
Assume second array is sorted
"""

def solution(a, b):
    b.sort()
    
    arr = []

    pos = 0
    for i in range(len(a)):
        for j in range(pos, len(b)):
            print (a[i], b[j], i, j)
            if a[i] == b[j]:
                arr.append(a[i])
                break
            if b[i] > a[j]:
                break
            pos += 1
            

    print (arr)

a = [13, 27, 35, 40, 49, 55, 59]
b = [17, 35, 39, 40, 55, 58, 60]
solution(a, b)