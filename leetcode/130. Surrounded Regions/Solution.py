class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = len(board) - 1
        if row <= 0:
            return
        col = len(board[0]) - 1
        quene = []
        for i in range(0, row):
            if (board[i][0]) == "O":
                quene.append((i, 0))
            if (board[i][col]) == "O":
                quene.append((i, col))
        for j in range(0, col+1):
            if (board[0][j]) == "O":
                quene.append((0, j))
            if (board[row][j]) == "O":
                quene.append((row, j))
                
        # 广度优先搜索
        while quene:
            x, y = quene.pop(0)
            board[x][y] = "A"
            if x > 0 and board[x-1][y] == "O":
                quene.append((x-1, y))
            if x < row and board[x+1][y] == "O":
                quene.append((x+1, y))
            if y > 0 and board[x][y-1] == "O":
                quene.append((x, y-1))
            if y < col and board[x][y+1] == "O":
                quene.append((x, y+1))
        
        for i in range(0, row+1):
            for j in range(0, col+1):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "A":
                    board[i][j] = "O"
