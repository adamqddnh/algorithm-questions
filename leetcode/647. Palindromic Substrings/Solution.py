class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # DP方法
        dp = [[0] * len(s) for _ in range(len(s))]
        result = 0
        for j in range(0, len(s)):
            for i in range(0, j+1):
                if i == j:
                    dp[i][j] = 1
                    result += 1
                elif j - i == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                    result += 1
                elif j - i > 1 and s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = 1
                    result += 1
        return result
