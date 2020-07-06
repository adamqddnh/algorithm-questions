class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1]
        pointer2, pointer3, pointer5 = 0, 0, 0
        while len(dp) < n:
            temp2 = dp[pointer2] * 2
            temp3 = dp[pointer3] * 3
            temp5 = dp[pointer5] * 5
            minTemp = min(temp2, temp3, temp5)
            if minTemp is temp2:
                pointer2 += 1
                if (dp[-1] < minTemp):
                    dp.append(minTemp)
            if minTemp is temp3:
                pointer3 += 1
                if (dp[-1] < minTemp):
                    dp.append(minTemp)
            if minTemp is temp5:
                pointer5 += 1
                if (dp[-1] < minTemp):
                    dp.append(minTemp)
        return dp[-1]
