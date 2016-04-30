# O(n^2)

def printPairs(array):
    for i in range(0, len(array)):
        for j in range(0, len(array)):
            print (array[i], ', ', array[j])

printPairs([1,2,3,4,5])