class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        self.result = []
        for i in range(1, 10):
            self.dfs(i, N-1, K)
        if N == 1:
            self.result.append(0)
        return self.result
    
    def dfs(self, number, length, K):
        if length == 0:
            self.result.append(number)
            return
        tempLast = number % 10
        if tempLast + K < 10:
            self.dfs(number * 10 + tempLast + K, length - 1, K)
        if K != 0 and tempLast - K >= 0:
            self.dfs(number * 10 + tempLast - K, length - 1, K)
            
