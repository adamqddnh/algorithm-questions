class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si, ti = 0, 0
        if len(s) > len(t):
            return False

        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                si += 1
            ti += 1
        return si == len(s)
