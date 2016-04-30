"""
Given an array of distinct integer values, 
count the number of pairs of integers that have difference k. 
For example, given the array {1, 7, 5, 9, 2 ,12, 3} and difference k = 2, 
there are four pairs with difference 2: (1, 3), (3, 5), (5, 7), (7, 9)
"""



def solution_bruteforce(array, k):
    count = 0
    for i, ielem in enumerate(array):
        for j, jelem in enumerate(array):
            temp = abs(ielem - jelem)
            if temp == k and ielem < jelem:
                count += 1
    return count




def remove_duplicate_sorted(array, n):
    duplicates = [ 0 for i in range(n)]
    temp = array[0]
    for i in range(1, n):
        if array[i] != temp:
            temp = array[i]
        else:
            duplicates[i] = 1

    for i in range(n - 1, 0, -1):
        if duplicates[i]:
            array.pop(i)

    return array


def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint+1:],item)

def solution(array, k):
    n = len(array)
    count = 0
    array.sort()
    array = remove_duplicate_sorted(array, n)

    for i, elem in enumerate(array):
        if (binarySearch(array, elem + k)):
            count += 1
    return count


array = [1, 7, 5, 9, 2 ,12, 3]
print ( solution(array, 2) )
