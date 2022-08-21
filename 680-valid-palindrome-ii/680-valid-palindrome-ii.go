/*
Time - O(n)
Space - O(1)
*/
func isValidPalindrome(s string, i,j int) bool {
    for i<j {
        if s[i]!=s[j]{
            return false
        }
        i++
        j--
    }
    return true
}

func validPalindrome(s string) bool {
    i:=0
    j:=len(s)-1
    for i<j {
        if s[i]!=s[j] {
            return isValidPalindrome(s, i+1, j) || isValidPalindrome(s, i, j-1)
        }
        i++
        j--
    }
    return true
}