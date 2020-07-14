# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        self.result = True
        self.dfs(p, q)
        return self.result
        
    def dfs(self, p, q):
        if not self.result:
            return
        if not p and not q:
            return
        elif p and q:
            if p.val != q.val:
                self.result = False
                return
            self.dfs(p.left, q.left)
            self.dfs(p.right, q.right)
        else:
            self.result = False
        return
