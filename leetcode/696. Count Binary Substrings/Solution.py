class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        preNum = 0
        curNum = 0
        preStr = ""
        for word in s:
            if preStr == "":
                preStr = word
                curNum = 1
                continue
            if word == preStr:
                curNum += 1
            else:
                result += min(preNum, curNum)
                preNum = curNum
                curNum = 1
            preStr = word
        return result + min(preNum, curNum)
