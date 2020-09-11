class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        maxNum = 1
        minNum = 1
        for i in range(0, len(nums)):
            if nums[i] < 0:
                maxNum, minNum = minNum, maxNum
            maxNum = max(maxNum * nums[i], nums[i])
            minNum = min(minNum * nums[i], nums[i])
            result = max(result, maxNum)
            
        return result
