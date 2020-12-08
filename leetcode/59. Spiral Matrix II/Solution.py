class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0 for i in range(n)] for j in range(n)]
        direction = 1 # up: 0; right: 1; down: 2; left: 3
        left, right, up, down = 0, n - 1, 0, n - 1
        row, line = 0, 0
        number = 1
        while number <= n * n:
            # Right
            for line in range(left, right + 1):
                result[up][line] = number
                number += 1
            up += 1
            # Down
            for row in range(up, down + 1):
                result[row][right] = number
                number += 1
            right -= 1
            # Left
            for line in range(right, left - 1, -1):
                result[down][line] = number
                number += 1
            down -= 1
            # Up
            for row in range(down, up - 1, -1):
                result[row][left] = number
                number += 1
            left += 1
        return result
