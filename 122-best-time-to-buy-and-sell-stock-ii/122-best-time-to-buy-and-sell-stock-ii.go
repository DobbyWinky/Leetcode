func maxProfit(prices []int) int {
    buy:=0
    sell:=1
    ans:=0
    max:=0
    for sell<len(prices) {
        if prices[sell]<prices[sell-1] {
            buy=sell
            sell++
            ans+=max
            max=0
        }else {
            if prices[sell]-prices[buy]>max {
                max=prices[sell]-prices[buy]
            }
            sell++
        }
    }
    ans+=max
    return ans
}