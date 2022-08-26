/*
Time - O(26*n)
Space - O(26)
*/
func characterReplacement(s string, k int) int {
    count:=make([]int, 26)
    left:=0
    right:=0
    maxWindow:=0
    for right<len(s) {
        count[s[right]-'A']++
        for left<=right && right-left+1-max(count)>k {
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

func max(count []int) int {
    maxi:=0
    for i:=0;i<26;i++ {
        if count[i]>maxi {
            maxi=count[i]
        }
    }
    return maxi
}