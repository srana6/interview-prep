import unittest

def insertion_sort(array):
	if not array: return
	n = len(array)

	for j in range(1, n):
		key = array[j]
		i = j - 1

		while i >= 0 and array[i] > key:
			array[i + 1] = array[i]
			i -= 1
		array[i + 1] = key





class Test(unittest.TestCase):
	def test_sort(self):
		data = [1, 8, 3, 6, 99, 2, 2]

		result = insertion_sort(data)
		print (data)


unittest.main()