import unittest

def find_peak_slow(arr):
	peak = 0
	for i in range(len(arr)):
		if arr[i] > arr[peak]:
			peak = i
	return arr[peak]


def _find_peak_fast(arr, start, end):		
	if start > end:
		return None

	mid = (start + end)//2

	if mid - 1 >= start and arr[mid] < arr[mid - 1]:
		return _find_peak_fast(arr, start, mid - 1)
	elif mid + 1 < end and arr[mid] < arr[mid + 1]:
		return _find_peak_fast(arr, mid + 1, end)
	else:
		return arr[mid]

def find_peak_fast(arr):
	return _find_peak_fast(arr, 0, len(arr))


class Test(unittest.TestCase):
	data = [
		([6, 7, 4, 3, 2 , 1, 4, 5], 7),
		([1, 3, 5, 6, 7, 9], 9),
		([i for i in range(1000000)], 999999)]

	def test_find_peak_fast(self):
		for (test_input, expected) in self.data:
			self.assertEqual(find_peak_fast(test_input), expected)

	def test_find_peak_slow(self):
		for (test_input, expected) in self.data:
			self.assertEqual(find_peak_slow(test_input), expected)

unittest.main()


