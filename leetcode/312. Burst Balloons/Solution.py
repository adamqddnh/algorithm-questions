class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        dp = [([0] * len(nums)) for i in range(len(nums))]
        
        def countRange(start, end):
            maxNumber = 0
            for i in range(start + 1, end):
                left = dp[start][i]
                right = dp[i][end]
                mid = left + nums[start] * nums[i] * nums[end] + right
                if mid > maxNumber:
                    maxNumber = mid
            dp[start][end] = maxNumber
        
        for n in range(2, len(nums)):
            for start in range(0, len(nums) - n):
                countRange(start, start + n)
                
        return dp[0][-1]
