class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        if not prices:
            return result
        buy = prices[0]
        for price in prices:
            if price > buy:
                result = max(result, price - buy)
            buy = min(buy, price)
        return result
