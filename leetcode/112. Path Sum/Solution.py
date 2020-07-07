# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root and sum == 0:
            return False
        self.result = False
        self.total = sum
        self.dfs(root, 0)
        return self.result

    def dfs(self, root, tempSum):
        if self.result or not root:
            return
        if not root.left and not root.right:
            if self.total == tempSum + root.val:
                self.result = True
            return
        self.dfs(root.left, tempSum + root.val)
        self.dfs(root.right, tempSum + root.val)
