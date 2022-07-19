func prefixCount(words []string, pref string) int {
    count:=0
    for _, word :=range words {
        if len(word)>=len(pref) && word[:len(pref)]==pref {
            count++
        }
    }
    return count
}