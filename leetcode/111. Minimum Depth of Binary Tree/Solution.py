# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = sys.maxint
        self.dfs(root, 1)
        return 0 if not root else self.result

    def dfs(self, root, depth):
        if not root:
            return
        if not root.left and not root.right:
            self.result = min(self.result, depth)
        if root.left:
            self.dfs(root.left, depth+1)
        if root.right:
            self.dfs(root.right, depth+1)
