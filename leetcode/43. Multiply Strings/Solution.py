class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0 for _ in range(0, len(num1) + len(num2))]
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(0, len(num1)):
            for j in range(0, len(num2)):
                result[i+j] += int(num1[i]) * int(num2[j])
        for i in range(0, len(result)-1):
            result[i+1] += result[i] / 10
            result[i] %= 10
        while result[-1] == 0 and len(result) > 1:
            result = result[:-1]
        return ''.join([str(number) for number in result[::-1]])
