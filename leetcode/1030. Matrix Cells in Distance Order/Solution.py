class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        maxLength = R + C + 1
        distance = [[] for i in range(0, maxLength)]
        for i in range(0, R):
            for j in range(0, C):
                temp = abs(r0 - i) + abs(c0 - j)
                distance[temp].append([i, j])
        result = []
        for i in range(0, maxLength):
            for temp in distance[i]:
                result.append(temp)
        return result
