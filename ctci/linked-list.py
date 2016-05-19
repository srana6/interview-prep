import unittest

class Node(object):
	val = None
	next = None

	def __init__(self, val):
		self.val = val

	def show(self):
		print (self.val)

	def appendToTail(self, val):
		new = Node(val)
		aux = self

		while aux.next is not None:
			aux = aux.next
		aux.next = new
		return True

	@staticmethod
	def deleteNode(node, val):
		aux = node
		if aux.val == val:
			return aux.next

		while aux.next is not None:
			if aux.next.val == val:
				aux.next = aux.next.next
				return node
			aux = aux.next
		return node



class Test(unittest.TestCase):
	dataRoot = 10
	dataChild = [2, 1, 4, 5]

	def setUp(self):
		print ('Test')

	def test_NodeClass(self):
		root = Node(self.dataRoot)
		self.assertEqual(root.val, self.dataRoot)

		for child in self.dataChild:			
			self.assertTrue(root.appendToTail(child))


	def test_NodeDeletion(self):
		root = Node(self.dataRoot)
		for child in self.dataChild:			
			root.appendToTail(child)

		self.assertIsInstance(Node.deleteNode(root, 5), Node)

if __name__ == '__main__':
	unittest.main()
