class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        number = math.sqrt(num)
        return int(number) * int(number) == num
