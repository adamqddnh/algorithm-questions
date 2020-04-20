class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        i = 0
        while i < len(A) and i < K:
            if A[i] < 0:
                A[i] = -A[i]
            elif A[i] == 0:
                return sum(A)
            else:
                if i > 0 and A[i] > A[i-1]:
                    A[i], A[i-1] = A[i-1], A[i]
                A[i] = A[i] * (-1 if (K - i) % 2 == 1 else 1)
                i = K
            i += 1
            
        if i < K:
            A[-1] = A[-1] * (-1 if (K - i) % 2 == 1 else 1)
            
        return sum(A)
