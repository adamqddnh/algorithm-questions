class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastWord = ""
        result = 0
        temp = 1
        for word in s:
            if word == lastWord:
                temp += 1
                result = max(result, temp)
            else:
                lastWord = word
                temp = 1
                result = max(result, 1)
        return result
