import "strings"
func isPalindrome(s string) bool {
    i:=0
    j:=len(s)-1
    s=strings.ToLower(s)
    for i<j {
        if !unicode.IsLetter(rune(s[i])) && !unicode.IsDigit(rune(s[i])) {
            i++
            continue
        }
        if !unicode.IsLetter(rune(s[j])) && !unicode.IsDigit(rune(s[j])){
            j--
            continue
        }
        if s[i]!=s[j] {
            return false
        }
        i++
        j--
    }
    return true
}