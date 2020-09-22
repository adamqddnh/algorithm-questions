class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        car = [0] * 1001
        maxPosition = 0
        for i in range(0, len(trips)):
            car[trips[i][1]] += trips[i][0]
            car[trips[i][2]] -= trips[i][0]
            maxPosition = max(maxPosition, trips[i][2])
        for i in range(1, maxPosition+1):
            car[i] += car[i-1]
            if car[i] > capacity:
                return False
        return True
