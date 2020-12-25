class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        total = m + n - 1
        result = []
        isLeft = True
        for i in range(0, total):
            if not isLeft:
                for row in range(0, min(m, i) + 1):
                    if row < m and i - row < n:
                        result.append(matrix[row][i-row])
            else:
                for col in range(0, min(n, i) + 1):
                    if i - col < m and col < n:
                        result.append(matrix[i-col][col])
            isLeft = not isLeft
        return result
