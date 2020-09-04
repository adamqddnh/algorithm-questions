# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.result = []
        if not root:
            return []
        self.dfs(root, [str(root.val)])
        return self.result
        
    def dfs(self, root, tempResult):
        if not root:
            return
        if not root.left and not root.right:
            self.result.append("->".join(tempResult))
            return
        
        if root.left:
            self.dfs(root.left, tempResult + [str(root.left.val)])
        if root.right:
            self.dfs(root.right, tempResult + [str(root.right.val)])
