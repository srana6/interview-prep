"""
Swap minimum and maximum element 
in an integer array.
"""
import sys

def getMinIndex(array):
	minIndex = 0
	for i in range(len(array)):
		if array[i] < array[minIndex]:			
			minIndex = i
	return minIndex

def getMaxIndex(array):
	maxIndex = 0
	for i in range(len(array)):
		if array[i] > array[maxIndex]:			
			maxIndex = i
	return maxIndex

def swap(array, minIndex, maxIndex):
	array[minIndex], array[maxIndex] = array[maxIndex], array[minIndex]
	return array

def swapMinMax(array):
	minIndex = getMinIndex(array)
	maxIndex = getMaxIndex(array)
	swap(array, minIndex, maxIndex)
	return array


test = [100, 4, 6, 7, 10, 30, 20]
swapped = swapMinMax(test)

print (swapped)