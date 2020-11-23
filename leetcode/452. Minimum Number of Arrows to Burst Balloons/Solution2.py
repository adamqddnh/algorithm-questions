class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = 0
        if not points:
            return result

        points.sort(key = lambda x: x[0])
        current = points[0]
        for point in points:
            if self.checkInterval(current, point):
                current = self.mergeInterval(current, point)
            else:
                result += 1
                current = point

        return result + 1

    def checkInterval(self, first, second):
        if first[0] > second[1] or first[1] < second[0]:
            return False
        return True

    def mergeInterval(self, first, second):
        return [max(first[0], second[0]), min(first[1], second[1])]
