class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sLength = len(s)
        tLength = len(t)
        if sLength > tLength:
            return False
        sHead, tHead = 0, 0
        while sHead < sLength and tHead < tLength:
            if s[sHead] == t[tHead]:
                sHead += 1
                tHead += 1
            else:
                tHead += 1
        return sHead >= sLength
