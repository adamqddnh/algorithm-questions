class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = 0
        odd = 1
        length = len(A)
        while max(even, odd) < length:
            while even < length and A[even] % 2 == 0:
                even += 2
            while odd < length and A[odd] % 2 != 0:
                odd += 2
            if max(even, odd) < length:
                A[even], A[odd] = A[odd], A[even]
        return A
