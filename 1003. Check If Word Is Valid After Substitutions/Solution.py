class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        while S.find('abc') > -1:
            S = S.replace('abc', '')
        return True if S == '' else False
