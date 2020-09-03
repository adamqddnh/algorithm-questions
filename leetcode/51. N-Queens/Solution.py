class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col = [0 for _ in range(0, n)]
        leftToRight = [0 for _ in range(0, n * 2 - 1)]
        rightToLeft = [0 for _ in range(0, n * 2 - 1)]
        self.result = []
        self.dfs(n, 0, col, leftToRight, rightToLeft, [])
        return self.formatResult(self.result, n)

    def dfs(self, maxLevel, level, col, leftToRight, rightToLeft, tempResult):
        if level >= maxLevel:
            self.result.append(tempResult)
            return
        for i in range(0, maxLevel):
            if col[i] == 0 and leftToRight[i - level + maxLevel - 1] == 0 and rightToLeft[i + level] == 0:
                col[i] = 1
                leftToRight[i - level + maxLevel - 1] = 1
                rightToLeft[i + level] = 1
                self.dfs(maxLevel, level + 1, col, leftToRight, rightToLeft, tempResult + [i])
                col[i] = 0
                leftToRight[i - level + maxLevel - 1] = 0
                rightToLeft[i + level] = 0
    
    def formatResult(self, results, n):
        res = []
        for result in results:
            tempRes = []
            for number in result:
                tempStr = "." * number + "Q" + "." * (n - number - 1)
                tempRes.append(tempStr)
            res.append(tempRes)
        return res
