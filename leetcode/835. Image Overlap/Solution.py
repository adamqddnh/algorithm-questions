class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        resultDict = collections.defaultdict(int)
        aList = self.mapToCoordinate(A)
        bList = self.mapToCoordinate(B)
        for aCoordinate in aList:
            for bCoordinate in bList:
                resultDict[(aCoordinate[0] - bCoordinate[0]) * 50 + aCoordinate[1] - bCoordinate[1]] += 1
        try:
            return max(resultDict.values())
        except:
            return 0
        
    def mapToCoordinate(self, numberMap):
        result = []
        for i in range(0, len(numberMap)):
            for j in range(0, len(numberMap[0])):
                if numberMap[i][j] == 1:
                    result.append((i, j))
        return result
