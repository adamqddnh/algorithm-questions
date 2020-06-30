# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x, y):
#        """
#        :type x : int, y : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        n, m = binaryMatrix.dimensions()
        
        left, right = 0, m
        while left < right:
            mid = left + (right - left) / 2
            if all([binaryMatrix.get(i, mid) == 0 for i in range(0, n)]):
                left = mid + 1
            else:
                right = mid
        return left if left < m else -1
