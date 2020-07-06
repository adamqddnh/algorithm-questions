class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp = [[0] * len(obstacleGrid[0]) for _ in range(0, len(obstacleGrid))]
        dp[0][0] = 1 ^ obstacleGrid[0][0]
        for i in range(0, len(obstacleGrid)):
            for j in range(0, len(obstacleGrid[0])):
                if i is 0 and j is 0:
                    continue
                if obstacleGrid[i][j] is 1:
                    dp[i][j] = 0
                else:
                    left = 0 if j is 0 else dp[i][j-1]
                    up = 0 if i is 0 else dp[i-1][j]
                    dp[i][j] = left + up
        return dp[-1][-1]
