class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0 for i in range(0, len(B))] for j in range(0, len(A))]
        result = 0
        for i in range(0, len(A)):
            for j in range(0, len(B)):
                if A[i] == B[j]:
                    dp[i][j] = 1 if i == 0 or j == 0 else dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
        return max(max(row) for row in dp)
