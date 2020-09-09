class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.dfs(candidates, target, [])
        return self.result

    def dfs(self, candidates, target, tempRes):
        if target < 0:
            return
        if target == 0:
            self.result.append(tempRes)

        for i in range(0, len(candidates)):
            self.dfs(candidates[i:], target - candidates[i], tempRes + [candidates[i]])
