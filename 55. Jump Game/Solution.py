class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        
        arr = [i for i in range(0, len(nums))]
        
        arr[0] = nums[0]
        if arr[0] == 0:
            return False
        
        length = len(nums)
        for i in range(1, length):
            arr[i] = max(arr[i-1], arr[i]+nums[i])
            if arr[i] == i and i < length-1:
                return False
        
        return True
