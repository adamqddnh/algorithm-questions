class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        left, right = 0, len(nums)-1
        while left <= right:
            while right >= 0 and nums[right] == val:
                right -= 1
            while left <= right and nums[left] != val:
                res += 1
                left += 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        return res
