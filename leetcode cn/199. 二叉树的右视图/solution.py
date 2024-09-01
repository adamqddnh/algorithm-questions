# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = [root]
        while queue:
            tempQueue = []
            res.append(queue[-1].val)
            for node in queue:
                if node.left is not None:
                    tempQueue.append(node.left)
                if node.right is not None:
                    tempQueue.append(node.right)
            queue = tempQueue

        return res
