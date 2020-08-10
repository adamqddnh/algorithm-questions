# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.result = []
        if not root:
            return self.result
        self.dfs(root, sum, [])
        return self.result
        
    def dfs(self, rootNode, total, tempArray):
        if not rootNode:
            return
        if not rootNode.left and not rootNode.right:
            if total == rootNode.val:
                tempArray.append(rootNode.val)
                self.result.append(tempArray)
            return
        if rootNode.left:
            self.dfs(rootNode.left, total - rootNode.val, tempArray + [rootNode.val])
        if rootNode.right:
            self.dfs(rootNode.right, total - rootNode.val, tempArray + [rootNode.val])
