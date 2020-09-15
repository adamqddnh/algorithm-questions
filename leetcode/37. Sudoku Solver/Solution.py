class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = [set() for i in range(0, 9)]
        col = [set() for i in range(0, 9)]
        grid = [set() for i in range(0, 9)]
        positions = {}
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != '.':
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    grid[(i // 3) * 3 + (j // 3)].add(board[i][j])
                else:
                    positions[i * 9 + j] = (i, j)
        print positions

        def dfs(position):
            if position == 81:
                return True
            if not positions.get(position, None):
                return dfs(position + 1)
            i = position // 9
            j = position % 9
            for num in range(1, 10):
                strNum = str(num)
                if (strNum in row[i]) or (strNum in col[j]) or (strNum in grid[(i // 3) * 3 + (j // 3)]):
                    continue
                else:
                    row[i].add(strNum)
                    col[j].add(strNum)
                    grid[(i // 3) * 3 + (j // 3)].add(strNum)
                    board[i][j] = strNum
                    if (dfs(position + 1)):
                        return True
                    row[i].remove(strNum)
                    col[j].remove(strNum)
                    grid[(i // 3) * 3 + (j // 3)].remove(strNum)

        dfs(0)
