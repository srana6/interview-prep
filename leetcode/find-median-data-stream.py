from heapq import *

class MedianFinder:
    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0





mf = MedianFinder()
mf.addNum(3)
mf.addNum(5)
mf.addNum(10)
mf.addNum(1)
mf.addNum(20)
print ('median', mf.findMedian())

#mf.findMedian()


arr = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
arr.sort()
print (arr)