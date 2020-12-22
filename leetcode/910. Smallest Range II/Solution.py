class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        minNum, maxNum = A[0], A[-1]
        result = maxNum - minNum
        for i in range(0, len(A)-1):
            a, b = A[i], A[i+1]
            result = min(result, max(maxNum-K, a+K) - min(minNum+K, b-K))
        return result
