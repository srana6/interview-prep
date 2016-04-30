def pairSum(a, b):
    return a + b

def pairSumSequence(n):
    sum = 0;    
    for i in range(0, n):
        sum += pairSum(i, i + 1)

    return sum

print (pairSumSequence(3))