class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]
        for i in range(0, rowIndex):
            result.append(0)
            tempResult = result[:]
            for j in range(0, len(result)):
                tempResult[j] = result[j] if j == 0 else result[j] + result[j-1]
            result = tempResult[:]
        return result
