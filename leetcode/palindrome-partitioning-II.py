"""
def partition(collection):
	if len(collection) == 1:
		yield [ collection ]
		return

	first = collection[0]
	for smaller in partition(collection[1:]):
		# insert `first` in each of the subpartition's subsets
		for n, subset in enumerate(smaller):
			yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
		# put `first` in its own subset 
		yield [ [ first ] ] + smaller


something = list(range(1,4))

print (something)

for n, p in enumerate(partition(something), 1):
	print(n, sorted(p))
"""


# Incomplete
def minCut(s):
	cut = [x for x in range(-1,len(s))]
	print (cut)

	for i in range(0,len(s)):
		for j in range(i,len(s)):
			if s[i:j] == s[j:i:-1]:
				cut[j+1] = min(cut[j+1],cut[i]+1)
	return cut[-1]

def minCut(s):
	if s == s[::-1]: return 0
	lens = len(s)
	for i in range(1, lens):
		if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
			return 1

	



sol = minCut("abccbad")
print(sol)