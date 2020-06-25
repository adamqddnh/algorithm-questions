class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = True
        for i in range(0, len(nums)):
            while i+1 != nums[i]:
                if nums[i] == nums[nums[i]-1]:
                    return nums[i]
                else:
                    temp = nums[nums[i]-1]
                    nums[nums[i]-1] = nums[i]
                    nums[i] = temp            
