func truncateSentence(s string, k int) string {
    ans:=""
    for i:=0;i<len(s);i++ {
        if s[i]!=' ' {
            ans+=string(s[i])
        }else {
            k--
            if k>0 {
                ans+=" "
            }else {
                break
            }
        }    
    }
    return ans
}