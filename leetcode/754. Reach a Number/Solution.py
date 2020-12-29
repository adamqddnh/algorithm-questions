class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        result = 0
        num = 1
        while target > 0:
            target -= num
            result += 1
            if target < 0:
                if target % 2 == 0:
                    return result
                else:
                    return result + 1 + (1 if num % 2 != 0 else 0)
            num += 1
        return result
