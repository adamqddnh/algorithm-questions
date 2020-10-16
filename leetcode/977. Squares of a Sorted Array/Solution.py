class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        length = len(A)
        result = [0] * length
        head, tail, position = 0, length - 1, length - 1
        while head <= tail:
            if abs(A[head]) < abs(A[tail]):
                result[position] = A[tail] * A[tail]
                tail -= 1
            else:
                result[position] = A[head] * A[head]
                head += 1
            position -= 1

        return result
