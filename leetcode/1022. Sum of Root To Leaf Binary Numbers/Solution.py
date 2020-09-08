# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.dfs(root, [])
        return self.result
        
    def dfs(self, root, tempRes):
        if not root:
            return
        if not root.left and not root.right:
            tempRes = tempRes + [root.val]
            self.result += self.calculate(tempRes)
            return
        if root.left:
            self.dfs(root.left, tempRes + [root.val])
        if root.right:
            self.dfs(root.right, tempRes + [root.val])
            
    def calculate(self, arr):
        l = len(arr) - 1
        temp = 1
        result = 0
        for i in range(l, -1, -1):
            result += arr[i] * temp
            temp *= 2
        return result
