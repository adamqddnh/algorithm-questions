class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsMap = {}
        for i in range(0, len(nums)):
            if numsMap.has_key(target-nums[i]):
                return [numsMap[target-nums[i]], i]
            else:
                numsMap[nums[i]] = i
        return []
