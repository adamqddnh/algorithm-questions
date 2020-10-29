# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.dfs(root, 0)
        return self.result

    def dfs(self, root, number):
        if not root:
            return

        if not root.left and not root.right:
            self.result += number * 10 + root.val
            return

        if root.left:
            self.dfs(root.left, number * 10 + root.val)
        if root.right:
            self.dfs(root.right, number * 10 + root.val)
