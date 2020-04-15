class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        number = abs((minutes / 60.0) * 360 - (hour % 12) * 30.0 - minutes / 60.0 * 30)
        return min(number, 360.0 - number)
