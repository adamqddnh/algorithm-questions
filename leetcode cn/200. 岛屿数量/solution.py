class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == "1":
                    self.find(grid, row, col)
                    res += 1
        return res

    def find(self, grid, row, col):
        grid[row][col] = "0"
        if row > 0 and grid[row-1][col] == "1":
            self.find(grid, row-1, col)
        if col > 0 and grid[row][col-1] == "1":
            self.find(grid, row, col-1)
        if row < len(grid)-1 and grid[row+1][col] == "1":
            self.find(grid, row+1, col)
        if col < len(grid[0])-1 and grid[row][col+1] == "1":
            self.find(grid, row, col+1)
        
