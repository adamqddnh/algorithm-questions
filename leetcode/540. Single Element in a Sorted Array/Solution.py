class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right) / 2
            print mid
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            
            if (right - mid) % 2 == 1:
                if nums[mid] == nums[mid+1]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] == nums[mid+1]:
                    left = mid
                else:
                    right = mid
        
        return nums[left]
