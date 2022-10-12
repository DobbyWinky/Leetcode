func shortestDistance(wordsDict []string, word1 string, word2 string) int {
    index:=make(map[string][]int)
    for i:=0;i<len(wordsDict);i++ {
        index[wordsDict[i]]=append(index[wordsDict[i]], i)
    }
    first:=index[word1]
    second:=index[word2]
    ans:=9999999
    for i:=0;i<len(first);i++ {
        for j:=0;j<len(second);j++ {
            ans=min(ans, abs(first[i]-second[j]))
        }
    }
    return ans
}

func min(i,j int) int {
    if i<j {
        return i
    }
    return j
}

func abs(i int) int {
    if i<0{
        return -i
    }
    return i
}