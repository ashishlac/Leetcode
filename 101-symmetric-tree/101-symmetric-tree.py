# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
                return True
        
        def rec(l,r):
            if not l and not r:
                return True
            if l and r:
                return l.val == r.val and rec(l.left,r.right) and rec(l.right, r.left)
            return False
        
        return rec(root.left,root.right)
            
        