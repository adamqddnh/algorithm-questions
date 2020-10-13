class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        charDict = collections.defaultdict(int)
        if len(A) != len(B):
            return False
        
        diff = 0
        multi = False
        diffA, diffB = "", ""
        for i in range(0, len(A)):
            if A[i] != B[i]:
                diff += 1
                diffA += A[i]
                diffB += B[i]
            if diff > 2:
                return False
            charDict[A[i]] += 1
            if charDict[A[i]] >= 2:
                multi = True
        return True if (diff == 2 and diffA == diffB[::-1]) or (diff == 0 and multi) else False
