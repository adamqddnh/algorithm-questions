class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        lineArr = [[-1] * len(B) for i in range(0, len(A))]

        def run(i, j):
            if i < 0 or j < 0:
                return 0
            if lineArr[i][j] != -1:
                return lineArr[i][j]
            if A[i] == B[j]:
                lineArr[i][j] = run(i-1, j-1) + 1
            else:
                lineArr[i][j] = max(run(i-1, j), run(i, j-1))
            return lineArr[i][j]
            
        return run(len(A)-1, len(B)-1)
