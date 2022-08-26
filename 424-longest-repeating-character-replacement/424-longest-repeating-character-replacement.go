/*
Time - O(26*n)
Space - O(26)
*/
func characterReplacement(s string, k int) int {
    count:=make([]int, 26)
    left:=0
    right:=0
    maxWindow:=0
    maxFreq:=0
    for right<len(s) {
        count[s[right]-'A']++
        maxFreq=max(maxFreq, count[s[right]-'A'])
        for right-left+1-maxFreq>k {
            count[s[left]-'A']--
            left++
        }
        if right-left+1>maxWindow {
            maxWindow=right-left+1
        }
        right++
    }
    return maxWindow
}

func max(i,j int) int {
    if i>j {
        return i
    }
    return j
}