class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        result = []
        for i in range(lo, hi+1):
            temp = i
            times = 0
            while temp != 1:
                temp = temp / 2 if temp % 2 == 0 else temp * 3 + 1
                times += 1
            result.append((i, times))
        result.sort(key = lambda x:(x[1],x[0]))
        return result[k-1][0]
