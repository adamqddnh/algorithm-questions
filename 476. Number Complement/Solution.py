class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = 0
        n = num
        while num > 0:
            temp = (temp << 1) + 1
            num >>= 1
        return n ^ temp
