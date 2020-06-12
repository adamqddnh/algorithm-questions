class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        nums.sort()
        for i in range(0, len(nums)-2):
            # Duplicate removal
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            self.twoSum(nums[i+1:], 0-nums[i])
        return self.result
            
    def twoSum(self, nums, target):
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] + nums[j] == target:
                self.result.append([-target, nums[i], nums[j]])
                while i < j and nums[i] == nums[i+1]:
                    i += 1
                while i < j and nums[j-1] == nums[j]:
                    j -= 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
        return
