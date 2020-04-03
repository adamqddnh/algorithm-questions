class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        dp = [[0 for i in range(0, n)] for j in range(0, m)]
        for i in range(0, m):
            for j in range(0, n):
                if i is 0 or j is 0:
                    print i, j
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
