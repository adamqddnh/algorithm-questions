# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return not root or self.dfs(root.left, root.right)

    def dfs(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True

        if not left or not right or left.val != right.val:
            return False

        return self.dfs(left.left, right.right) and self.dfs(left.right, right.left)
