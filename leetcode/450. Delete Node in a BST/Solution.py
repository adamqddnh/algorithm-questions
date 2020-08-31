# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left != None and root.right != None:
                root.val = self.findMin(root.right).val
                root.right = self.deleteNode(root.right, root.val)
            else:
                root = root.right if not root.left else root.left
        return root
                
    def findMin(self, root):
        if not root:
            return root
        temp = root
        while temp.left:
            temp = temp.left
        return temp
