# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
	K = [[0 for x in range(W+1)] for x in range(n+1)]
 
	# Build table K[][] in bottom up manner
	for i in range(n+1):
		for w in range(W+1):
			if i==0 or w==0:
				K[i][w] = 0
			elif wt[i-1] <= w:
				K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
			else:
				K[i][w] = K[i-1][w]
	
	for row in (K):
		print (row)

	return K[n][W]

def variant_knapsack(W, weights, values, n):
	weight = 0
	value = 0
	content = []

	for i in range(n):
		if weight + weights[i] <= W:
			weight += weights[i]
			value += values[i]
			content.append([values[i]])
	return value



class Item(object):
	def __init__(self, weight, value):
		self.weight = weight
		self.value = value
		self.ratio = weight / value

	def __repr__(self):
		return  "(%s, %s, %s)" % (self.weight, self.value, self.ratio)

	def __eq__(self, other):
		return self.ratio == other.ratio

	def __lt__(self, other):
		return self.ratio < other.ratio

def fractional_knapsack(W, items):
	n = len(items)
	items.sort()

	weight = 0
	value = 0

	for i in range(n):
		if weight + items[i].weight < W:
			weight += items[i].weight
			value += items[i].value
		else:
			remaining = W - weight
			value += items[i].value * (remaining / items[i].weight)
			break
	return value

 
# Driver program to test above function
# val = [60, 100, 120]
# wt = [10, 20, 30]

wt = [10, 20, 30, 60]
val = [120, 100, 60, 10]

W = 25
n = len(val)
print(knapSack(W, wt, val, n))

print(variant_knapsack(W, wt, val, n))


items = []
items.append(Item(30, 120))
items.append(Item(10, 60))
items.append(Item(20, 100))


print (fractional_knapsack(50, items))