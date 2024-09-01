class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[0] * 9 for _ in range(9)]
        col = [[0] * 9 for _ in range(9)]
        block = [[0] * 9 for _ in range(9)]

        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == ".":
                    continue
                num = int(board[i][j]) - 1
                zone = i // 3 * 3 + j // 3
                row[i][num] += 1
                col[j][num] += 1
                block[zone][num] += 1
                if row[i][num] > 1 or col[j][num] > 1 or block[zone][num] > 1:
                    return False

        return True
