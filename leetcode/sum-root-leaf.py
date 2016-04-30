"""
Sum Root to Leaf Numbers


Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3

The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def traverse(self, root, stack, total):
        if not root:
            return 0

        stack.append(root.val)
        if not root.left and not root.right:
            total = total + int(''.join(map(str, stack)))
            stack.pop()
            return total

        left = self.traverse(root.left, stack, total) 
        right = self.traverse(root.right, stack, total)

        stack.pop()
        return left + right
            

    def sumNumbers(self, root):
        stack = []
        return self.traverse(root, stack, 0)


"""
root = TreeNode(1)
root.right = TreeNode(4)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(6)
root.right.right.right = TreeNode(7)
root.right.right.right.left = TreeNode(1)
root.right.right.right.left.left = TreeNode(2)
root.right.right.right.left.right = TreeNode(4)
"""

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(3)


sol = Solution().sumNumbers(root)
print (sol)
        



