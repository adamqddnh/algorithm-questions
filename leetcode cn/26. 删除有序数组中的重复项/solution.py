class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = len(nums)
        if len(nums) <= 1:
            return res

        left, right = 0, 1
        lastNum = nums[0]
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
                res -= 1
            else:
                left += 1
                nums[left] = nums[right]
                right += 1

        return res
