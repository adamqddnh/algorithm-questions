class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        left = [0 for i in range(0, len(seats))]
        right = [0 for i in range(0, len(seats))]
        
        # Left to right
        start = -1
        for i in range(0, len(seats)):
            if seats[i] == 1:
                start = i
                left[i] = 0
            else:
                left[i] = i - start if start >= 0 else sys.maxint
                
        start = len(seats)
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 1:
                start = i
                right[i] = 0
            else:
                right[i] = start - i if start < len(seats) else sys.maxint
                
        result = 0
        for i in range(0, len(left)):
            result = max(min(left[i], right[i]), result)
        return result
