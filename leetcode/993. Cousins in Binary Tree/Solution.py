# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        self.depthDict = collections.defaultdict(tuple)
        self.dfs(root, None, 0)
        xParent, xDepth = self.depthDict[x]
        yParent, yDepth = self.depthDict[y]
        return xDepth == yDepth and xParent != yParent
        
    def dfs(self, root, parent, level):
        if not root:
            return
        self.depthDict[root.val] = (parent, level)
        self.dfs(root.left, root, level+1)
        self.dfs(root.right, root, level+1)
