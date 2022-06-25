func firstPalindrome(words []string) string {
    for _, word :=range words {
        if isPalindrome(word) {
            return word
        }
    }
    return ""
}

func isPalindrome(word string) bool {
    i:=0
    j:=len(word)-1
    for i<j {
        if word[i]!=word[j] {
            return false
        }
        i++
        j--
    }
    return true
}