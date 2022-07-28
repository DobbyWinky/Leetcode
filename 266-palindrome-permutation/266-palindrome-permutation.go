func canPermutePalindrome(s string) bool {
    hash:=make(map[byte]int)
    for i:=0;i<len(s);i++ {
        hash[s[i]]++
    }
    one:=false
    if len(hash)==1 {
        return true
    }
    for _,v:=range hash {
        if v%2!=0 {
            if !one{
                one=true
            }else {
                return false
            }
        }
    }
    return true
}