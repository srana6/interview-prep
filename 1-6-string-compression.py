"""
Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabccccccaaa would become a2b1c5a3. If the "compressed" string would not
become smaller than the original string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a-z)

Example:
	aabccccccaaa
	a2b1c5a3

Analysis
	Remember character being looked and its frequency into an auxiliar variable
	Append those in a list, if the length becomes equal to, then return original
	Time: O(N)
	Space: O(N)
"""

def compress(string):
	compressed = []
	length_string = len(string)
	length_compressed = 0

	count_frequency = 0
	for i in range(length_string):
		count_frequency += 1

		if i + 1 == length_string or string[i] != string[i + 1]:
			compressed.append(string[i])
			compressed.append(str(count_frequency))

			length_compressed += 1 + len(str(count_frequency))
			count_frequency = 0

			if length_compressed >= length_string:
				return string

	return "".join(compressed)


string = "abcdefghjiklmnoqp"
result = compress(string)

print (result)

