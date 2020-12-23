class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        strNums = list(str(n))
        for i in range(len(strNums)-1, 0, -1):
            if strNums[i] > strNums[i-1]:
                start = i - 1
                end = i
                temp = strNums[start]
                for j in range(i, len(strNums)):
                    if strNums[j] > temp:
                        end = j
                    else:
                        break
                strNums[start], strNums[end] = strNums[end], strNums[start]
                result = int(''.join(strNums[:i] + strNums[i:][::-1]))
                return -1 if result > 2147483647 else result
        return -1
