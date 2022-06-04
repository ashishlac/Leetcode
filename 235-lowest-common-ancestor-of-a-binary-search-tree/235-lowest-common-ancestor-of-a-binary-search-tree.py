# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        curr=root
        parent=root
        while curr is not None:
            if curr.val == "null":
                return parent
            if curr.val == p.val or curr.val == q.val:
                return curr
            if p.val > curr.val:
                p_right=1
            elif p.val < curr.val:
                p_right= -1
            else:
                p_right = 0
            if q.val > curr.val:
                q_right=1
            elif q.val < curr.val:
                q_right= -1
            else:
                q_right = 0
            if p_right != q_right:
                return parent
            if p_right == 0:
                return p
            elif q_right == 0:
                return q
            if p_right > 0 and q_right > 0:
                curr=curr.right
            else:
                curr=curr.left
            
            parent=curr
            
        return 0