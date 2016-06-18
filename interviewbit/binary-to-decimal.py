"""
Given a binary number as a string. Convert this to an integer in decimal system.

"""

def convert(binary):
	if not binary: return 0
	size = len(binary)
	num = 0

	for i in range(size):
		idx = size - i - 1

		if binary[idx] == '1':
			num += pow(2, i)

	print (num)


num = "1111101"
convert(num)