type Codec struct {
}

// Encodes a list of strings to a single string.
func (codec *Codec) Encode(strs []string) string {
    ans:=""
    for _, str:=range strs{
        ans+=strconv.Itoa(len(str))+"#"
        ans+=str
    }
    return ans
}

// Decodes a single string to a list of strings.
func (codec *Codec) Decode(strs string) []string {
    ans:=make([]string, 0)
    i:=0
    for i<len(strs) {
        var count []byte
        for strs[i]!='#' {
            count=append(count, strs[i])
            i++
        }
        i++
        countInt, _:=strconv.Atoi(string(count))
        k:=0
        var ansStr []byte
        for k<countInt {
            ansStr=append(ansStr, strs[i])
            k++
            i++
        }
        ans=append(ans, string(ansStr))
    }
    return ans
}

// Your Codec object will be instantiated and called as such:
// var codec Codec
// codec.Decode(codec.Encode(strs));