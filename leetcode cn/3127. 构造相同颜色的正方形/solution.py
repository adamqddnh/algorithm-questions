class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        return self.check(0, 0, grid) or self.check(0, 1, grid) or self.check(1, 0, grid) or self.check(1, 1, grid)

    def check(self, i: int, j: int, grid: List[List[str]]) -> bool:
        record = defaultdict(int)
        record[grid[i][j]] += 1
        record[grid[i+1][j]] += 1
        record[grid[i][j+1]] += 1
        record[grid[i+1][j+1]] += 1
        return record['B'] != 2
        
