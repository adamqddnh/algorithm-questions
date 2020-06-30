# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        result = n
        while left <= right:
            mid = (left + right) / 2
            if isBadVersion(mid) is True:
                right = mid - 1
                result = min(result, mid)
            else:
                left = mid + 1
            
        return result
