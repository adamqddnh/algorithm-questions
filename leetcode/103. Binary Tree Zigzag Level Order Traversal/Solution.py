# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result

        queue = [root]
        result.append([root.val])
        times = 1
        while queue:
            tempQueue = []
            tempRes = []
            for eachNode in queue:
                if not eachNode:
                    continue
                if eachNode.left:
                    tempRes.append(eachNode.left.val)
                    tempQueue.append(eachNode.left)
                if eachNode.right:
                    tempRes.append(eachNode.right.val)
                    tempQueue.append(eachNode.right)
            if tempRes:
                if times % 2 == 0:
                    result.append(tempRes)
                else:
                    result.append(tempRes[::-1])
            queue = tempQueue[:]
            times += 1

        return result
