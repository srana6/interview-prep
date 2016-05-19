# O(n^2)

def printUnorderedPairs(array):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            print ("%s, %s" % (array[i], array[j]))

printUnorderedPairs([1,2,3,4,5])