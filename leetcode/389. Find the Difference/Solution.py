class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        charDict = collections.defaultdict(int)
        for ch in t:
            charDict[ch] += 1
        for ch in s:
            charDict[ch] -= 1
        for ch in charDict:
            if charDict[ch] > 0:
                return ch
        return ""
