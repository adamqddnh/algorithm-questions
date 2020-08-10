class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        i = 1
        for word in s[::-1]:
            result += (ord(word) - ord('A') + 1) * i
            i *= 26
        return result
