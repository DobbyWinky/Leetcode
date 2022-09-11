func breakPalindrome(palindrome string) string {
    pbyte:=[]byte(palindrome)
    if len(pbyte)==1 {
        return ""
    }
    for i:=0;i<len(pbyte)/2;i++ {
        if pbyte[i]!='a' {
            pbyte[i]='a'
            return string(pbyte)
        }
    }
    pbyte[len(pbyte)-1]='b'
    return string(pbyte)
}