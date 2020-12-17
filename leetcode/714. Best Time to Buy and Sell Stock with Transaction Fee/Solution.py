class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy = [0] * len(prices)
        sell = [0] * len(prices)
        buy[0] = -prices[0]

        for i in range(1, len(prices)):
            sell[i] = max(sell[i-1], buy[i-1] + prices[i] - fee)
            buy[i] = max(buy[i-1], sell[i-1] - prices[i])
        return sell[-1]
