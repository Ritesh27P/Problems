class Solution:
    def maxProfit(self, prices) -> int:
        res = 0
        buy, sell = 0, 1

        while sell < len(prices):
            if (prices[buy] < prices[sell]):
                profit = prices[sell] - prices[buy]
                res = max(profit, res)
            elif (prices[buy] > prices[sell]):
                buy = sell
                sell = buy
                continue

            sell += 1
        return res
            
        
        
            