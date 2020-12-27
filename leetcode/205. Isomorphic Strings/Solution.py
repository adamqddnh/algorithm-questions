class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict = {}
        tDict = {}
        for i in range(0, len(s)):
            if s[i] not in sDict and t[i] not in tDict:
                sDict[s[i]] = t[i]
                tDict[t[i]] = s[i]
            elif sDict.get(s[i], None) != t[i] or tDict.get(t[i], None) != s[i]:
                return False

        return True
