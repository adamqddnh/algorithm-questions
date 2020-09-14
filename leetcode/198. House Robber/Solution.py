class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        dp = [0 for i in range(0, len(nums))]
        for i in range(0, l):
            if i < 2:
                dp[i] = max(nums[:i+1])
            elif i == 2:
                dp[i] = max(dp[i-1] + dp[i-3], dp[i-2] + nums[i])
            else:
                dp[i] = max(dp[i-2], dp[i-3]) + nums[i]

        return 0 if not dp else max(dp)
