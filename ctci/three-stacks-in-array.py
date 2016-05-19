"""
Describe how you could use a single array to implement three stacks
"""

class Stacks(object):
	totalStacks = 2

	def __init__(self, stackSize):
		self.stackSize = stackSize
		self.array = [None for i in range(self.stackSize * self.totalStacks)]
		self.size = [0 for i in range(self.totalStacks)]

	def push(self, stack, value):
		if not self.isFull(stack):			
			self.size[stack] += 1
			idx = self.indexOf(stack)			
			self.array[idx] = value

	def isFull(self, stack):
		return (self.size[stack] == self.stackSize)

	def indexOf(self, stack):
		offset = stack * self.stackSize
		size = self.size[stack]
		return offset + size - 1

	def show(self):
		print (self.array)


stacks = Stacks(10)
stacks.push(0, 1)
stacks.push(0, 2)
stacks.push(0, 3)
stacks.push(0, 4)
stacks.push(0, 5)
stacks.push(1, 5)
stacks.show()