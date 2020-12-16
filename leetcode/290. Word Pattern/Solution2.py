class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(words):
            return False

        patternToWords = {}
        wordsToPattern = {}

        for i in range(len(pattern)):
            if patternToWords.has_key(pattern[i]) and patternToWords[pattern[i]] != words[i]:
                return False
            else:
                patternToWords[pattern[i]] = words[i]

            if wordsToPattern.has_key(words[i]) and wordsToPattern[words[i]] != pattern[i]:
                return False
            else:
                wordsToPattern[words[i]] = pattern[i]
                
        return True
