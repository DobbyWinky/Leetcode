func calculateTime(keyboard string, word string) int {
    index:=make(map[byte]int)
    for i:=0;i<len(keyboard);i++ {
        index[keyboard[i]]=i
    }
    initPos:=0
    ans:=0
    for i:=0;i<len(word);i++ {
        ans+=abs(initPos-index[word[i]])
        initPos=index[word[i]]
    }
    return ans
}

func abs(i int) int {
    if i<0 {
        return -i
    }
    return i
}