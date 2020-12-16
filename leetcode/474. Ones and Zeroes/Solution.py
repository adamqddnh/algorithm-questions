class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n+1) for _ in range(m+1)]
        for eachStr in strs:
            oneNum = eachStr.count('1')
            zeroNum = eachStr.count('0')
            for i in range(m, zeroNum - 1, -1):
                for j in range(n, oneNum - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeroNum][j - oneNum])
        return dp[-1][-1]
