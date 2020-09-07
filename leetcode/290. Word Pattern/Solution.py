class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(pattern) != len(words):
            return False
        wordsDict = {}
        wordsSet = set()
        for i in range(0, len(pattern)):
            if pattern[i] not in wordsDict:
                if words[i] not in wordsSet:
                    wordsSet.add(words[i])
                    wordsDict[pattern[i]] = words[i]
                else:
                    return False
            else:
                if wordsDict[pattern[i]] != words[i]:
                    return False
        return True
