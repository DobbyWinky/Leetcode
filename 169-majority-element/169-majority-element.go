func majorityElement(nums []int) int {
    freq:=make(map[int]int)
    maxEle:=0
    maxFreq:=0
    for _, num:=range nums {
        freq[num]++
        if freq[num]>maxFreq {
            maxFreq=freq[num]
            maxEle = num
        }
    }
    return maxEle
}