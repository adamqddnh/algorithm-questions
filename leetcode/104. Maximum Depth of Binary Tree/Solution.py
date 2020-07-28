# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        if not root:
            return self.result
        else:
            self.dfs(root, 0)
        return self.result
        
    def dfs(self, root, level):
        if not root:
            return
        self.result = max(self.result, level + 1)
        if root.left:
            self.dfs(root.left, level + 1)
        if root.right:
            self.dfs(root.right, level + 1)
