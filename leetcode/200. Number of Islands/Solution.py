class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        result = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == '1':
                    self.find(grid, i, j)
                    result += 1
        return result
                    
    def find(self, grid, row, col):
        grid[row][col] = '0'
        if (row > 0 and grid[row-1][col] == '1'):
            self.find(grid, row-1, col)
        if (col > 0 and grid[row][col-1] == '1'):
            self.find(grid, row, col-1)
        if (row < len(grid)-1 and grid[row+1][col] == '1'):
            self.find(grid, row+1, col)
        if (col < len(grid[0])-1 and grid[row][col+1] == '1'):
            self.find(grid, row, col+1)
