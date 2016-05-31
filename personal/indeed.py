# Complete the function below.
import math

memo = {}

def isSquare(num):    
    for i in range(int(math.sqrt(num)) + 1):
        if i * i == num:
            return True
    return False


def calculate(start, end):
    count = 0
    for num in range(start, end + 1):
        if num not in memo:
            memo[num] = isSquare(num)
        
        if memo[num]:
            count  += 1            
    return count

def  getMinimumUniqueSum(arr):
    for element in arr:
        start, end = list(map(int, element.strip().split()))
        total_squares = calculate(start, end)
        print (total_squares)

getMinimumUniqueSum(["3 9", "3 102"])