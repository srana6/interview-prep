import unittest

"""
Reserve array in place
"""

def reverse(array):
	start = 0
	end = len(array) - 1

	while start < end:
		array[start], array[end] = array[end], array[start]

		start += 1
		end -= 1






class Test(unittest.TestCase):
	def test_merging(self):
		data = [
			(['h', 'o', 'l', 'a'], ['a', 'l', 'o', 'h'])
		]

		for (array, output) in data:
			reverse(array)
			self.assertEqual(array, output)

unittest.main()