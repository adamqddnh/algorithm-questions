class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        for i in range(0, len(s)):
            if s[i] not in dic1: 
                dic1[s[i]] = t[i]
            elif dic1[s[i]] != t[i]:
                return False
                
            if t[i] not in dic2:
                dic2[t[i]] = s[i]
            elif dic2[t[i]] != s[i]:
                return False

        return True
