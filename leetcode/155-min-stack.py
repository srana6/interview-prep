"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

"""

class MinStack(object):

	MAX = float('inf')

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.last = -1
		self.minimum = []
		self.stack = []
		

	def push(self, x):
		"""
		:type x: int
		:rtype: void
		"""
		currMin = self.minimum[self.last] if self.minimum else self.MAX
		currMin = min(currMin, x)

		self.stack.append(x)
		self.minimum.append(currMin)
		

	def pop(self):
		"""
		:rtype: void
		"""
		if self.stack:
			self.stack.pop()
			self.minimum.pop()

	def top(self):
		"""
		:rtype: int
		"""
		if self.stack:
			return self.stack[self.last]
		return None
		

	def getMin(self):
		"""
		:rtype: int
		"""

		if self.minimum:
			return self.minimum[self.last]
		return None
