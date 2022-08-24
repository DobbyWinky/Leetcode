func lengthOfLongestSubstring(s string) int {
    wordMap:=make(map[byte]int)
    i:=0
    j:=0
    window:=0
    for j<len(s) {
        if val, ok:=wordMap[s[j]]; ok {
            i=max(i, val)
        }
        window=max(window, j-i+1)
        wordMap[s[j]]=j+1
        j++
    }
    return window
}

func max(i,j int) int {
    if i>j {
        return i
    }
    return j
}