# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidSequence(self, root, arr):
        """
        :type root: TreeNode
        :type arr: List[int]
        :rtype: bool
        """
        return self.dfs(root, arr, 0)
        
    def dfs(self, root, arr, level):
        if not root:
            return False
        if not root.left and not root.right:
            if level == len(arr)-1 and arr[level] == root.val:
                return True
            else:
                return False
        if level >= len(arr) or arr[level] != root.val:
            return False
        
        left = False
        right = False
        if root.left:
            left = self.dfs(root.left, arr, level+1)
        if root.right:
            right = self.dfs(root.right, arr, level+1)
        
        return left or right
        
