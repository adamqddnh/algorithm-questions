class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        resultDict = {}
        for number in arr:
            if number in resultDict:
                resultDict[number] += 1
            else:
                resultDict[number] = 1
        result = -1
        for k, v in resultDict.items():
            if k == v and k > result:
                result = k
        return result
