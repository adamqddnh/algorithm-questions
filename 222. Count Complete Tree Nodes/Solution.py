# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.dfs(root)
        return self.result
        
    def dfs(self, root):
        if root is None:
            return
        self.result += 1
        if root.left is not None:
            self.dfs(root.left)
        if root.right is not None:
            self.dfs(root.right)
