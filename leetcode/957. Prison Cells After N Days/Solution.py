class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        if N is 0:
            return cells
        else:
            N = N % 14 + 14
        cellsLength = len(cells)
        result = cells[:]
        for i in range(0, N):
            for j in range(1, cellsLength-1):
                result[j] = cells[j-1] ^ cells[j+1] ^ 1
            result[0], result[-1] = 0, 0
            cells = result[:]
        return result
        
