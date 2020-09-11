class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.dfs(1, 9, k, n, [])
        return self.result

    def dfs(self, start, end, k, target, tempRes):
        if target < 0 or k < 0:
            return
        if target == 0 and k == 0:
            self.result.append(tempRes)
            return

        for i in range(start, end + 1):
            if i <= target:
                self.dfs(i+1, end, k-1, target-i, tempRes + [i])
            else:
                break
