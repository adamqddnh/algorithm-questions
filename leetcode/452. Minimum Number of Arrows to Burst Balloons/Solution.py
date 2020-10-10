class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda x : x[0])
        start, end = -sys.maxint - 1, -sys.maxint - 1
        result = 0
        for point in points:
            if point[0] > end:
                result += 1
                start = point[0]
                end = point[1]
            else:
                start = max(start, point[0])
                end = min(end, point[1])
        return result
