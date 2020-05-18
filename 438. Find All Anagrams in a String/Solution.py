class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        
        sDict = {}
        pDict = {}
        result = []
        for i in range(0, 26):
            sDict[chr(ord('a') + i)] = 0
            pDict[chr(ord('a') + i)] = 0
        
        for i in range(0, len(p)):
            sDict[s[i]] += 1
            pDict[p[i]] += 1
        if sDict == pDict:
            result.append(0)
        
        pLength = len(p)
        for i in range(pLength, len(s)):
            sDict[s[i-pLength]] -= 1
            sDict[s[i]] += 1
            if sDict == pDict:
                result.append(i - pLength + 1)
        
        return result
