inf = float("inf")

numbers = [1, 2, 3, -1, -80]
numbers = [10, -inf]

def getMax(numbers):
	if not numbers: return None
	first = numbers[0]
	second = getMax(numbers[1:])

	if second is None or first >= second: return first
	else: return second

sol = getMax(numbers)
print (sol)



"""


class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None


n1 = Node(1)
n2 = Node(2)
n3 = Node(4)

n1.next = n2
n2.next = n3

def invert(root):
	if not root: return None

	aux = root.next
	root.next = 


"""


table = {}
table["1"] = "hello"


for key, value in table.items():
	print (key, value)