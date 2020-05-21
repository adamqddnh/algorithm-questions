# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.result = None
        self.dfs(root, 0)
        return self.result
        
    def dfs(self, root, num):
        if self.result:
            return num
        if not root:
            return num;
        if root.left:
            num = self.dfs(root.left, num)
        num += 1
        if num == self.k:
            self.result = root.val
            return num
        if root.right:
            num = self.dfs(root.right, num)
        return num
