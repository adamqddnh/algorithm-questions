class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        """
        0: down
        1: right
        2: up
        3: left
        """
        direction = 0
        positionX, positionY = 0, 0
        for i in range(0, 4):
            for word in instructions:
                if word == 'L':
                    direction = (direction + 1) % 4
                elif word == 'R':
                    direction = (direction - 1) % 4
                elif word == 'G':
                    if direction % 2 == 0:
                        positionX += direction - 1
                    else:
                        positionY += direction - 2
            if positionX == 0 and positionY == 0:
                return True
        return False
