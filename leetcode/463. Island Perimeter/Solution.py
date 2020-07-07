class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        downMax, rightMax = len(grid)-1, len(grid[0])-1
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] is 1:
                    up = 1 if i is 0 or grid[i-1][j] is 0 else 0
                    down = 1 if i is downMax or grid[i+1][j] is 0 else 0
                    left = 1 if j is 0 or grid[i][j-1] is 0 else 0
                    right = 1 if j is rightMax or grid[i][j+1] is 0 else 0
                    result += up + down + left + right
        return result
