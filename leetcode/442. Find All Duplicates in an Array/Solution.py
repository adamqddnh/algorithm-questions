class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = set()
        for i in range(0, len(nums)):
            while (nums[i] != i+1):
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
                if nums[i] == nums[nums[i]-1] and nums[i] != i+1:
                    result.add(nums[i])
                    break
        return list(result)
