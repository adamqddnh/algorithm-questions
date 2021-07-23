class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        ranges.sort(lambda x,y:cmp(x[0],y[0]))
        for each in ranges:
            if each[0] > left:
                return False
            if left <= each[1]:
                left = each[1] + 1
            if left > right:
                return True
            
        return False
