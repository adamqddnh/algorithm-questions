# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.result = []
        self.bfs(root, 0)
        return self.result[::-1]
        
    def bfs(self, root, level):
        if not root:
            return None
        if (len(self.result) - 1) < level:
            self.result.append([root.val])
        else:
            self.result[level].append(root.val)
        
        if root.left:
            self.bfs(root.left, level+1)
        if root.right:
            self.bfs(root.right, level+1)
        return None
