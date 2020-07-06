class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        for i in range(len(digits)-1, 0, -1):
            if digits[i] >= 10:
                digits[i] %= 10
                digits[i-1] += 1
            else:
                break
        if digits[0] >= 10:
            digits[0] %= 10
            digits = [1] + digits
        return digits
