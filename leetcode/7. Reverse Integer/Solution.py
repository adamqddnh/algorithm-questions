class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            result = int(str(x)[::-1])
        else:
            result = -int(str(x)[::-1][:-1])
        return result if -2 ** 31 <= result <= 2 ** 31 - 1 else 0
