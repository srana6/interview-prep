import unittest


class Error(Exception):
	pass


class Stack(object):
	def __init__(self):
		self.stack = []
		self.operations = set(["push", "print"])

	def execute(self, operation = "", value = None):
		if operation == 'push' and value is not None:
			self.push(value)

		elif operation == 'print':
			self.println()
		return None


	def push(self, value):
		value = int(value)
		self.stack.append(value)


	def println(self):
		if not self.stack:
			raise Error("Invalid")
		elem = self.stack.pop()
		print (elem)


	def get_last_two(self):
		if len(self.stack) < 2:
			raise Error("Invalid")
		return (self.stack.pop(), self.stack.pop())


class OperatorFactory(object):
	def __init__(self):
		self.operators = set(["add", "sub"])

	def get_class(self, operator = ""):
		if operator == 'add':
			return Add()

		elif operator == 'sub':
			return Sub()

		return None


class Operator(object):
	def execute(self, a, b):
		pass


class Add(Operator):
	def execute(self, a, b):
		return a + b


class Sub(Operator):
	def execute(self, a, b):
		return a - b


class Interpreter(object):
	def __init__(self):
		self.stack = Stack()
		self.operatorFactory = OperatorFactory()


	def parse(self, instruction):
		splitted = instruction.split()
		if len(splitted) == 1:
			splitted.append(None)
		return splitted


	def evaluate(self, instructions):
		if not instructions: return 

		try:
			for instruction in instructions:
				instr, val = self.parse(instruction)

				if instr in self.operatorFactory.operators:
					_operator = self.operatorFactory.get_class(instr)
					a, b = self.stack.get_last_two()
					result = _operator.execute(a, b)					
					self.stack.push(result)

				elif instr in self.stack.operations:
					self.stack.execute(instr, val)

		except Error as err:
			print ("Error", err)



class Test(unittest.TestCase):
	def test_testing(self):
		interpreter = Interpreter()
		instructions = [
			"push 100",
			"push 1",
			"push 2",
			"print",
			"add",
			"print",
			"push 5",			
			"add"
		]

		interpreter.evaluate(instructions)



unittest.main()