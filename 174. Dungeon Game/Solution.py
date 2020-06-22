class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        # DP is the minimum rest health when knight reaches room(i, j)
        dp = [[sys.maxint for i in range(0, len(dungeon[0])+1)] for j in range(0, len(dungeon)+1)]
        maxRow = len(dungeon) - 1
        maxCol = len(dungeon[0]) - 1
        dp[maxRow][maxCol] = 1 if dungeon[maxRow][maxCol] >= 0 else -dungeon[maxRow][maxCol]+1
        for i in range(maxRow, -1, -1):
            for j in range(maxCol, -1, -1):
                if i == maxRow and j == maxCol:
                    continue
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
        print dp
        return dp[0][0]
