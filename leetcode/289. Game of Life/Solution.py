class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        row, col = len(board), len(board[0])
        for i in range(0, row):
            for j in range(0, col):
                self.countBoard(board, i, j, row, col)
        for i in range(0, row):
            for j in range(0, col):
                board[i][j] >>= 1
                
    def countBoard(self, board, i, j, row, col):
        temp = 0
        for k1 in range(-1, 2):
            for k2 in range(-1, 2):
                if k1 == 0 and k2 == 0:
                    continue
                if i + k1 < 0 or i + k1 >= row or j + k2 < 0 or j + k2 >= col:
                    continue
                temp += board[i+k1][j+k2] % 2
        if board[i][j] == 1:
            if temp == 2 or temp == 3:
                board[i][j] = 3
        else:
            if temp == 3:
                board[i][j] = 2
