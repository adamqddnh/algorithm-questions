# 1431. Kids With the Greatest Number of Candies
# 1431. 拥有最多糖果的孩子

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxCandy = max(candies)
        return [candies[i] + extraCandies >= maxCandy for i in range(0, len(candies))]
