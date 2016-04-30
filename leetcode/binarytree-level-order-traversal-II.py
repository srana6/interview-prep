"""

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},

"""

import unittest
from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


class Solution(object):
    def levelOrderBottom(self, root):
        if not root: return []
        queue = deque([(root, 1)])
        result = []
        temp = []
        current = 0

        while queue:
            node, level = queue.popleft()
            if level != current and temp:
                result.insert(0, temp)
                temp = []
                current = level
            temp.append(node.val)
            
            if node.left: queue.append((node.left, level + 1))
            if node.right: queue.append((node.right, level + 1))
        if temp: result.insert(0, temp)
        return result

class Test(unittest.TestCase):
    data = [
        ('[5,4,7,3,null,2,null,-1,null,9]', True)
    ]

    def test_level_ob(self):
        for (nums, expected) in self.data:
            res = Solution().levelOrderBottom(deserialize(nums))

unittest.main()