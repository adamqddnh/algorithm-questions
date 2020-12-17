class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        result = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            else:
                if prices[i] - fee > minPrice:
                    result += prices[i] - fee - minPrice
                    minPrice = prices[i] - fee
            
        return result
