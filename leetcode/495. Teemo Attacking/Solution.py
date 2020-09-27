class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        result = 0
        timeMin = 0
        timeMax = 0
        for time in timeSeries:
            if timeMax < time:
                result += timeMax - timeMin
                timeMin = time
                timeMax = time + duration
            elif timeMax >= time:
                timeMax = time + duration
        result += timeMax - timeMin
        return result
