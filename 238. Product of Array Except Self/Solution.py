class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1 for i in range(0, len(nums))]
        right = [1 for i in range(0, len(nums))]
        
        for i in range(1, len(nums)):
            left[i] = nums[i-1] * left[i-1]
        for i in range(len(nums)-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]
        return [left[i] * right[i] for i in range(0, len(nums))]
