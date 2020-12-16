# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def __init__(self):
        self.pre = float('-inf')
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        if self.pre >= root.val:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)
