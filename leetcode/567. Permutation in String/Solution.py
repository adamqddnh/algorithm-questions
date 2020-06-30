class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        
        s1Dict = {}
        s2Dict = {}

        for i in range(0, 26):
            s1Dict[chr(ord('a') + i)] = 0
            s2Dict[chr(ord('a') + i)] = 0
        
        for i in range(0, len(s1)):
            s1Dict[s1[i]] += 1
            s2Dict[s2[i]] += 1
        if s1Dict == s2Dict:
            return True
        
        s1Length = len(s1)
        for i in range(s1Length, len(s2)):
            s2Dict[s2[i-s1Length]] -= 1
            s2Dict[s2[i]] += 1
            if s1Dict == s2Dict:
                return True
        
        return False
