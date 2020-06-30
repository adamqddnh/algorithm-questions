class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n >= 1:
            if n == 1:
                return True
            if n % 2 == 1:
                return False
            n = n // 2
        return False
