class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        charDict = {}
        for i in range(0, len(s)):
            if s[i] in charDict:
                charDict[s[i]] = -1
            else:
                charDict[s[i]] = i
        print charDict
        result = len(s)
        for char in charDict.keys():
            if charDict[char] >= 0 and charDict[char] < result:
                result = charDict[char]
        
        return -1 if result == len(s) else result
