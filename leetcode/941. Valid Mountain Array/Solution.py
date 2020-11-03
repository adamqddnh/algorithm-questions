class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        start = 0
        end = len(A) - 1
        while start < end and A[start] < A[start + 1]:
            start += 1
        while start < end and A[end - 1] > A[end]:
            end -= 1
        return start == end and start != 0 and end != len(A) - 1
