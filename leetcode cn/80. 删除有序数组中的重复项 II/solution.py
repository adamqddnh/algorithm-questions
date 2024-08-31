class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = len(nums)
        if len(nums) <= 1:
            return res

        left, right = 0, 1
        res = 2
        for i in range(2, len(nums)):
            if nums[i] == nums[left]:
                continue
            else:
                nums[res] = nums[i]
                left = right
                right = res
                res += 1

        return res
