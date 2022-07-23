func digitCount(num string) bool {
    hash:=make(map[int]int)
    for i:=0;i<len(num);i++ {
        hash[int(num[i]-'0')]++
    }
    for i:=0;i<len(num);i++ {
        if hash[i]!=int(num[i]-'0') {
            return false
        }
    }
    return true
}