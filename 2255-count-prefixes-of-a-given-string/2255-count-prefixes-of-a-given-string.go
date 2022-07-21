func countPrefixes(words []string, s string) int {
    ans:=0
    n:=len(s)
    for _, word:=range words {
        if len(word)<=n && s[:len(word)]==word {
            ans++
        }
    }
    return ans
}