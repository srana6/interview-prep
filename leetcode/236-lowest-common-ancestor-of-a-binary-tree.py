"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as 
the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, 
since a node can be a descendant of itself according to the LCA definition.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def covers(self, root, node):
        if not root: return False
        if root == node: return True
        
        return self.covers(root.left, node) or self.covers(root.right, node)
    
    def lowestCommonAncestorHelper(self, root, p, q):
        if not root: return None
        if root == p or root == q:
            return root
            
        left = self.lowestCommonAncestorHelper(root.left, p, q)
        right = self.lowestCommonAncestorHelper(root.right, p, q)
        
        if left and right:
            return root
        
        if left: return left
        if right: return right
        
        return None
        
    # solution 1
    def lowestCommonAncestor(self, root, p, q):
        if not root: return None
        if self.covers(root, p) and self.covers(root, q):
            return self.lowestCommonAncestorHelper(root, p, q)
        
        return None



    # solution 2
    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
        
        return root if left and right else left or right