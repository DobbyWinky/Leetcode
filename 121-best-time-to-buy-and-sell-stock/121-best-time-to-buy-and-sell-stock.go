func maxProfit(prices []int) int {
    buy:=0
    sell:=1
    max:=0
    for sell<len(prices) {
        profit:=prices[sell]-prices[buy]
        if profit<0 {
            buy=sell
            sell++
            continue
        }
        if profit>max {
            max=profit
        }
        sell++
    }
    return max
}