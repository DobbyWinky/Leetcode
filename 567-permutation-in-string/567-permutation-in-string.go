func checkInclusion(s1 string, s2 string) bool {
    if len(s2)<len(s1) {
        return false
    }
    count:=make([]int, 26)
    for i:=0;i<len(s1);i++ {
        count[s1[i]-'a']++
    }
    countX:=make([]int, 26)
    for k:=0;k<len(s1);k++ {
        countX[s2[k]-'a']++
    }
    matches:=0
    for i:=0;i<26;i++ {
        if count[i]==countX[i]{
            matches++
        }
    }
    if matches==26 {
        return true
    }
    i:=0
    j:=len(s1)
    for j<len(s2) {
        countX[s2[i]-'a']--
        if countX[s2[i]-'a']==count[s2[i]-'a'] {
            matches++
        }else if count[s2[i]-'a']-1==countX[s2[i]-'a']{
            matches--
        }
        countX[s2[j]-'a']++
        if countX[s2[j]-'a']==count[s2[j]-'a'] {
            matches++
        }else if count[s2[j]-'a']+1==countX[s2[j]-'a']{
            matches--
        }
        if matches==26 {
            return true
        }
        i++
        j++
    }
    return false
}