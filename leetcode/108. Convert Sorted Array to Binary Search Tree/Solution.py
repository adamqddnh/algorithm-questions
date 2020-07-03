# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        numsLength = len(nums)-1
        result = TreeNode(nums[numsLength / 2])
        result.left = self.sortedArrayToBST(nums[:numsLength / 2])
        result.right = self.sortedArrayToBST(nums[numsLength / 2 + 1:])
        return result
