class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        elif n is 2:
            return 1
        elif n is 3:
            return 2
        threeTimes = 0
        while n > 4:
            n -= 3
            threeTimes += 1
        return 3 ** threeTimes * n
