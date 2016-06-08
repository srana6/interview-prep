"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]


"""


from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        levels = []
        
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()

            if node:
                if level + 1 > len(levels):
                    levels.append([])

                levels[level].append(node.val)

                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))

        self.zigzagLevels(levels)
        return levels


    def zigzagLevels(self, levels):
        """ Reverses array of Odd levels """
        if not levels: return
        reverse = False
        n = len(levels)
        for i in range(n):
            if reverse:
                levels[i] = levels[i][::-1]
            reverse = not reverse
