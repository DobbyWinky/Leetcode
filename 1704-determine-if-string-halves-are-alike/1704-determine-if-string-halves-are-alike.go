func halvesAreAlike(s string) bool {
    s=strings.ToLower(s)
    vowels:=0
    consonants:=0
    for i:=0;i<len(s)/2;i++ {
        if isVowel(s[i]) {
            vowels++
        }else {
            consonants++
        }
    }
    
    for i:=len(s)/2;i<len(s);i++ {
        if isVowel(s[i]) {
            vowels--
        }else {
            consonants--
        }
    }
    return vowels==0 && consonants==0
}

func isVowel(s byte) bool {
    return s=='a' || s=='e' || s=='i' || s=='o' || s=='u'
}