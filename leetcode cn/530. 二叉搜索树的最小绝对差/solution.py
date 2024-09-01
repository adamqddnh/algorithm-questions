# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nums = []
        self.inOrder(root, nums)
        res = float('inf')
        for i in range(0, len(nums)-1):
            res = min(res, nums[i+1] - nums[i])
        return res

    def inOrder(self, root: Optional[TreeNode], res):
        if not root:
            return root

        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)
