class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.dfs([], nums)
        return self.result

    def dfs(self, current, last):
        if not last:
            self.result.append(current)
            return

        for i in range(0, len(last)):
            self.dfs(current + [last[i]], last[:i] + last[i+1:])
