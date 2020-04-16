class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        listA = [0 for i in range(3)]
        listB = [0 for i in range(3)]
        for i in range(0, len(moves)):
            if i % 2 == 0:
                listA[moves[i][0]] += 2 ** moves[i][1]
            else:
                listB[moves[i][0]] += 2 ** moves[i][1]
        
        if ((7 in listA) or (listA[0] & listA[1] & listA[2] >= 1)):
            return 'A'
        if ((7 in listB) or (listB[0] & listB[1] & listB[2] >= 1)):
            return 'B'
        
        if (listA[0] % 2 == 1 and listA[1] in [2, 3, 6, 7] and listA[2] >= 4):
            return 'A'
        if (listB[0] % 2 == 1 and listB[1] in [2, 3, 6, 7] and listB[2] >= 4):
            return 'B'
        
        if (listA[0] >= 4 and listA[1] in [2, 3, 6, 7] and listA[2] % 2 == 1):
            return 'A'
        if (listB[0] >= 4 and listB[1] in [2, 3, 6, 7] and listB[2] % 2 == 1):
            return 'B'

        return "Pending" if len(moves) < 9 else "Draw"
