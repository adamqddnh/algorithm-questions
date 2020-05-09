class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) <= 2:
            return True
        
        gradient = 0 if coordinates[0][0] - coordinates[1][0] == 0 else (coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0])
        for i in range(1, len(coordinates)):
            dy = coordinates[i-1][1] - coordinates[i][1]
            dx = coordinates[i-1][0] - coordinates[i][0]
            temp = 0 if dx == 0 else dy / dx
            if gradient != temp:
                return False
        return True
