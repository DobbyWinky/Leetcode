func replaceDigits(s string) string {
    var ans []byte
    for i:=0;i<len(s);i=i+2 {
        ans=append(ans, s[i])
        if i+1<len(s) {
            offset:=s[i+1]-'0'
            ans=append(ans, s[i]+byte(offset))
        }
    }
    return string(ans)
}