class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        for i in range(0, len(shift)):
            if shift[i][0] == 0:
                s = s[shift[i][1]:] + s[:shift[i][1]]
            else:
                s = s[-shift[i][1]:] + s[:-shift[i][1]]
        return s
