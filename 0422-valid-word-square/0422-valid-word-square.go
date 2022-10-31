func validWordSquare(words []string) bool {
    for i:=0;i<len(words);i++ {
        curr:=""
        for j:=0;j<len(words);j++ {
            if i<len(words[j]) {
                curr+=string(words[j][i])
            }
        }
        if curr!=words[i] {
            return false
        }
    }
    return true
}