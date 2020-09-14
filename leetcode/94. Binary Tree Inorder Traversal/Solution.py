# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        self.midOrder(root)
        return self.result

    def midOrder(self, root):
        if not root:
            return
        if root.left:
            self.midOrder(root.left)
        self.result.append(root.val)
        if root.right:
            self.midOrder(root.right)
