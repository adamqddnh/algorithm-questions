class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.numberSet = set()
        self.result = []
        self.dfs(candidates, target, [])
        return self.result

    def dfs(self, candidates, target, tempRes):
        if target < 0:
            return
        if target == 0:
            temp = ",".join(list(map(str, tempRes)))
            if temp not in self.numberSet:
                self.result.append(tempRes)
                self.numberSet.add(temp)
            return

        for i in range(0, len(candidates)):
            if candidates[i] <= target:
                self.dfs(candidates[i+1:], target - candidates[i], tempRes + [candidates[i]])
            else:
                break
