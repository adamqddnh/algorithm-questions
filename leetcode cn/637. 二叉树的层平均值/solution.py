# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        res = []
        queue = [root]
        while queue:
            tempQueue = []
            tempNums = []
            for node in queue:
                tempNums.append(node.val)
                if node.left:
                    tempQueue.append(node.left)
                if node.right:
                    tempQueue.append(node.right)
            res.append(sum(tempNums) / len(tempNums))
            queue = tempQueue

        return res
