class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 10:
            return N

        strNum = list(str(N))
        position = -1
        maxNum = -1
        for i in range(0, len(strNum) - 1):
            if maxNum < int(strNum[i]):
                maxNum = int(strNum[i])
                position = i
            if strNum[i] > strNum[i+1]:
                strNum[position] = str(int(strNum[position]) - 1)
                for j in range(position+1, len(strNum)):
                    strNum[j] = '9'
                break

        return int(''.join(strNum))
