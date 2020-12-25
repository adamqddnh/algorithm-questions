class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        gNum, sNum = 0, 0
        gn, sn = len(g), len(s)
        result = 0
        while gNum < gn:
            while sNum < sn and g[gNum] > s[sNum]:
                sNum += 1
            if sNum == sn:
                break
            result += 1
            gNum += 1
            sNum += 1
        return result
