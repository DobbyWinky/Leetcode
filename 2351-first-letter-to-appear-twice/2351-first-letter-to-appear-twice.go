func repeatedCharacter(s string) byte {
    hash:=make(map[byte]bool)
    for i:=0;i<len(s);i++ {
        if hash[s[i]] {
            return s[i]
        }
        hash[s[i]]=true
    }
    return '0'
}