func reversePrefix(word string, ch byte) string {
    var prefix []byte
    i:=0
    for i<len(word) && word[i]!=ch {
        prefix=append([]byte{word[i]}, prefix...)
        i++
    }
    if i<len(word) {
        prefix=append([]byte{word[i]}, prefix...)
        return string(prefix)+word[i+1:]
    }
    return word
}