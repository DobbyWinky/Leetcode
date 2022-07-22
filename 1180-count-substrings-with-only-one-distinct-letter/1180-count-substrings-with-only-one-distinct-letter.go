func countLetters(s string) int {
    count:=0
    for i:=0;i<len(s);i++ {
        for j:=i+1;j<len(s)+1;j++ {
            flag:=true
            for k:=0;k<len(s[i:j]);k++ {
                if s[i:j][k]!=s[i] {
                    flag=false
                    break
                }
            }
            if flag {
                count++
            }
        }
    }
    return count
}