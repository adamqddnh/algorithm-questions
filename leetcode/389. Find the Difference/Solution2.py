class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        chars = [0] * 26
        for st in s:
            chars[ord(st) - ord('a')] += 1
        for st in t:
            temp = ord(st) - ord('a')
            chars[temp] -= 1
            if chars[temp] < 0:
                return st
