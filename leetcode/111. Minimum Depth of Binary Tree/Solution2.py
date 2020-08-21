# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        rootList = []
        tempList = []
        tempList.append(root)
        result = 0
        while rootList or tempList:
            if not rootList:
                rootList = tempList[:]
                tempList = []
                result += 1
            if not rootList[0].left and not rootList[0].right:
                return result
            if rootList[0].left:
                tempList.append(rootList[0].left)
            if rootList[0].right:
                tempList.append(rootList[0].right)
            rootList = rootList[1:]
        return result
