class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        if not intervals:
            return result
        
        #Sort by first element
        intervals.sort(key = lambda x : x[0])
        last = intervals[0]
        for i in range (1, len(intervals)):
            if intervals[i][0] <= last[1]:
                last = [last[0], max(intervals[i][1], last[1])]
            else:
                result.append(last)
                last = intervals[i]
        result.append(last)
        return result
