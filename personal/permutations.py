def permutation(string, start = 0, end = None):
	if not string: return []
	if not end: end = len(string) - 1

	if start == end:
		print (string)

	else:
		for i in range(start, end + 1):
			string[start], string[i] = string[i], string[start]
			permutation(string, start + 1, end )
			string[start], string[i] = string[i], string[start]





def permutation(string, prefix = ""):
	if len(string) == 0:
		print (prefix)
	else:
		for i in range(len(string)):
			rem = string[:i] + string[i + 1:]
			permutation(rem, prefix + string[i])


string = "cat"
permutation(string)