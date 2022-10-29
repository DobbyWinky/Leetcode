func shortestDistance(wordDict []string, word1 string, word2 string) int {
    wordMap:=make(map[string][]int)
    for i:=0;i<len(wordDict);i++ {
        if wordDict[i]==word1 || wordDict[i]==word2 {
            wordMap[wordDict[i]]=append(wordMap[wordDict[i]], i+1)
        }
    }
    list1:=wordMap[word1]
    list2:=wordMap[word2]
    i:=0
    j:=0
    min:=999999999999
    for i<len(list1) && j<len(list2) {
        if abs(list1[i]-list2[j])<min {
            min=abs(list1[i]-list2[j])
        }
        if list1[i]==list2[j] {
            return 0
        }
        if list1[i]<list2[j] {
            i++
        }else {
            j++
        }
    }
    return min
}

func abs(i int) int {
    if i<0 {
        return -i
    }
    return i
}