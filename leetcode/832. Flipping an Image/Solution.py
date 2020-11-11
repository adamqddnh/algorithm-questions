class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(0, len(A)):
            A[i] = A[i][::-1]
            for j in range(0, len(A[i])):
                A[i][j] ^= 1
                
        return A
