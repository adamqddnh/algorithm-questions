class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
            
        x, y = 0, 0
        xMax, yMax = len(matrix)-1, len(matrix[0])-1
        totalCovered, totalNeed = 0, len(matrix) * len(matrix[0])
        covered = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        print covered
        result = []
        direct = 1 # 1: right, 2: down, 3: left, 4: up
        while totalCovered < totalNeed:
            # right
            if covered[x][y] == 0:
                totalCovered += 1
                result.append(matrix[x][y])
            covered[x][y] = 1
            if direct == 1:
                if y < yMax and covered[x][y+1] == 0:
                    y += 1
                else:
                    direct = 2
            elif direct == 2:
                if x < xMax and covered[x+1][y] == 0:
                    x += 1
                else:
                    direct = 3
            elif direct == 3:
                if y > 0 and covered[x][y-1] == 0:
                    y -= 1
                else:
                    direct = 4
            elif direct == 4:
                if x > 0 and covered[x-1][y] == 0:
                    x -= 1
                else:
                    direct = 1

        return result
