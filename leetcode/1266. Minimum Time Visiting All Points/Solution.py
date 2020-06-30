class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x = points[0][0]
        y = points[0][1]
        result = 0
        for i in range(1, len(points)):
            result += max(abs(points[i][0]-x), abs(points[i][1]-y))
            x = points[i][0]
            y = points[i][1]
        return result
