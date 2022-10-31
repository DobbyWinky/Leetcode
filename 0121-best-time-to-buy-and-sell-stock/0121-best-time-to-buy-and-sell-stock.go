/*
Time - O(n)
Space - O(1)
*/
func maxProfit(prices []int) int {
    buy:=0
    sell:=1
    maxProfit:=0
    for sell<len(prices) {
        profit:=prices[sell]-prices[buy]
        if profit>=0 {
            if profit>maxProfit {
                maxProfit=profit
            }
            sell++
        }else {
            buy=sell
            sell++
        }
    }
    return maxProfit
}