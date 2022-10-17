func checkIfPangram(sentence string) bool {
    count:=make([]bool, 26)
    for i:=0;i<len(sentence);i++ {
        count[sentence[i]-'a']=true
    }
    for i:=0;i<26;i++{
        if !count[i] {
            return false
        }
    }
    return true
}