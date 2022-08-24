func lengthOfLongestSubstring(s string) int {
    if len(s)==0 || len(s)==1 {
        return len(s)
    }
    i:=0
    j:=1
    wordMap:=make(map[byte]int)
    maxWindow:=1
    wordMap[s[0]]++
    for j<len(s) {
        wordMap[s[j]]++
        if wordMap[s[j]]==2 {
            for s[i]!=s[j] {
                wordMap[s[i]]--
                i++
            }
            wordMap[s[i]]--
            i++
        }
        maxWindow=max(maxWindow, j-i+1)
        j++
    }
    return maxWindow
}

func max(i,j int) int {
    if i>j {
        return i
    }
    return j
}