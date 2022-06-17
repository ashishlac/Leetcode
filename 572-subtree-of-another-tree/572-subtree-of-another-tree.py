# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        self.present = False
        def rec1(root,subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val == subRoot.val:
                res = rec2(root,subRoot)
                if res:
                    self.present = True
                    print("returning True")
                    return res
            rec1(root.left,subRoot)
            rec1(root.right,subRoot)
            print("coming to the end")
            return False
        def rec2(root,subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val == subRoot.val:
                return rec2(root.left,subRoot.left) and rec2(root.right, subRoot.right)
            else:
                return False

        rec1(root,subRoot)
        return self.present
        
              
    