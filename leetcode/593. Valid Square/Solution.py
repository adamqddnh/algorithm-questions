class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        return self.checkSquare(p1, p2, p3, p4) or self.checkSquare(p1, p2, p4, p3) or self.checkSquare(p1, p3, p2, p4)
        
    def distance(self, p1, p2):
        return (p1[1] - p2[1]) ** 2 + (p1[0] - p2[0]) ** 2
    
    def checkSquare(self, p1, p2, p3, p4):
        return self.distance(p1, p2) > 0 and self.distance(p1, p2) == self.distance(p2, p3) and self.distance(p2, p3) == self.distance(p3, p4) and self.distance(p3, p4) == self.distance(p4, p1) and self.distance(p1, p3) == self.distance(p2, p4)
