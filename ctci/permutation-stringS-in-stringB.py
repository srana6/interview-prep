def _count_letters(string):
	arr = {}
	for i, elem in enumerate(string):
		if string[i] not in arr:
			arr[elem] = 0
		arr[elem] += 1
	return arr

def find_permS_in_B(s, b):
	size_s = len(s)
	size_b = len(b)
	if size_s == 0 or size_b < size_s:
		return 0

	memo = _count_letters(s)
	pos = []

	for i in range(size_b):
		if b[i] in memo:
			if i + 4 > size_b:
				break		
			found = _count_letters(b[i:i + 4])		
			if memo == found:
				pos.append(i)

	return pos	

print (find_permS_in_B("abbc", "cbabadcbbabbcbabaabccbabc"))

