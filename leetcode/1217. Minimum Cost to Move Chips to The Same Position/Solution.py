class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        a, b = 0, 0
        for i in range(0, len(position)):
            if position[i] % 2 == 0:
                a += 1
            else:
                b += 1
        return min(a, b)
