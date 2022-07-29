func percentageLetter(s string, letter byte) int {
    count:=0.0
    for i:=0;i<len(s);i++ {
        if s[i]==letter {
            count++
        }
    }
    return int(count/float64(len(s))*100.00)
}