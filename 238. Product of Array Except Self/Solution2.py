class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        left = [1] * length
        right = [1] * length
        for i in range(1, length):
            left[i] = nums[i-1] * left[i-1]
            right[length-i-1] = nums[length-i] * right[length-i]
        return [left[i]*right[i] for i in range(0, length)]
