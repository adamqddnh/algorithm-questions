class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.buildString(S) == self.buildString(T)

    def buildString(self, string):
        result = ""
        i = len(string) - 1
        pound = 0
        while i >= 0:
            if string[i] == '#':
                pound += 1
            elif pound > 0:
                pound -= 1
            elif i >= 0:
                result += string[i]
            i -= 1

        return result
