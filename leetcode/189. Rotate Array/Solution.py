class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length <= 0 or k < 0:
            return
        
        k = k % length
        for i in range(0, length / 2):
            nums[i], nums[length - i - 1] = nums[length - i - 1], nums[i]

        length = k
        for i in range(0, length / 2):
            nums[i], nums[length - i - 1] = nums[length - i - 1], nums[i]

        length = len(nums)
        for i in range(k, (k + length) / 2):
            nums[i], nums[k + length - i - 1] = nums[k + length - i - 1], nums[i]
