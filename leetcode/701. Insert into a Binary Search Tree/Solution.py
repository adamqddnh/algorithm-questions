# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        result = root
        while root:
            if val <= root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    break
                else:
                    root = root.left
            else:
                if root.right is None:
                    root.right = TreeNode(val)
                    break
                else:
                    root = root.right
        return result
