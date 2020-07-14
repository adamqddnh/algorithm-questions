class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [0 for _ in range(0, len(triangle[-1]))]
        dp[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            iLength = len(triangle[i]) - 1
            for j in range(0, len(triangle[i])):
                if j is 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j is iLength:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        return min(triangle[-1])
