# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.result = 0
        self.dfs(root, False)
        return self.result
    
    def dfs(self, root, isLeft):
        if not root:
            return None
        if not root.left and not root.right and isLeft:
            self.result += root.val
            return None
        if root.left:
            self.dfs(root.left, True)
        if root.right:
            self.dfs(root.right, False)
