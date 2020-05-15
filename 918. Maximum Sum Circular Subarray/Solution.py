class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        INF = 30001
        total = 0
        curmax = 0
        maxsum = -INF
        curmin = 0
        minsum = INF
        for a in A:
            curmax = max(curmax + a, a)
            maxsum = max(maxsum, curmax)
            curmin = min(curmin + a, a)
            minsum = min(minsum, curmin)
            total += a
        return max(maxsum, total - minsum) if maxsum > 0 else maxsum
