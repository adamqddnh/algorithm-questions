class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        start = 0
        while start < len(S) - 1:
            if S[start] == S[start+1]:
                S = S[:start] + S[start+2:]
                start = start - 1 if start > 0 else 0
            else:
                start += 1
        return S
