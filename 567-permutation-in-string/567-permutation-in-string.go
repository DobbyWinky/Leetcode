func checkInclusion(s1 string, s2 string) bool {
    if len(s2)<len(s1) {
        return false
    }
    count:=make([]int, 26)
    for i:=0;i<len(s1);i++ {
        count[s1[i]-'a']++
    }
    windowSize:=len(s1)
    i:=0
    j:=windowSize-1
    for j<len(s2) {
        countIn:=make([]int, 26)
        for k:=i;k<=j;k++ {
            countIn[s2[k]-'a']++
        }
        equal:=true
        for i:=0;i<26;i++ {
            if countIn[i]!=count[i] {
                equal=false
                break
            }
        }
        if equal {
            return true
        }
        i++
        j++
    }
    return false
}