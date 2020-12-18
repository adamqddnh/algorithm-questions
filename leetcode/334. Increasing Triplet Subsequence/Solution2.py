class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = [1] * len(nums)
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[j] = max(dp[j], dp[i] + 1)
                if dp[j] >= 3:
                    return True
        return False
