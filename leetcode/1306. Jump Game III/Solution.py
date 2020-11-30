class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        self.flag = [True for _ in range(0, len(arr))]
        return self.dfs(start, arr)
        
    def dfs(self, current, arr):
        if arr[current] == 0:
            return True
        
        left = False
        if current - arr[current] >= 0 and self.flag[current - arr[current]]:
            self.flag[current - arr[current]] = False
            left = self.dfs(current - arr[current], arr)
            
        right = False
        if current + arr[current] < len(arr) and self.flag[current + arr[current]]:
            self.flag[current + arr[current]] = False
            right = self.dfs(current + arr[current], arr)
            
        return left or right
