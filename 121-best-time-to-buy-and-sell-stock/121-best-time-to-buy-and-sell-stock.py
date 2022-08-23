#Time - O(n)
#Space - O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        maxProfit=0
        while sell<len(prices):
            profit = prices[sell]-prices[buy]
            if profit<0:
                buy=sell
                sell+=1
            else:
                if profit>maxProfit:
                    maxProfit=profit
                sell+=1
        return maxProfit