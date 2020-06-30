class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
                
        dp = [[0 for i in range(0, n)] for j in range(0, m)]
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] is 1:
                    dp[i][j] = 0
                    continue
                if i is 0 and j is 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
