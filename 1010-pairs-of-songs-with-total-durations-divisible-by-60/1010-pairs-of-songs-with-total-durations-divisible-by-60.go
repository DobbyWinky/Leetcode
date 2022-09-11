/*
    Time - O()
*/
func numPairsDivisibleBy60(time []int) int {
    div:=make([]int, 60)
    count:=0
    for _, t:=range time {
        if t%60==0 {
            count+=div[t%60]
        }else {
            count+=div[60-t%60]
        }
        div[t%60]++
    }
    return count
}