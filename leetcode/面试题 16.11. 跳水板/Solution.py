class Solution(object):
    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        if k is 0:
            return []
        sumSet = set()
        for i in range(0, k+1):
            sumSet.add(shorter * i + longer * (k - i))
        return sorted(list(sumSet))
