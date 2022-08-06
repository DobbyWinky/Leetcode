/*
Time - O(n)
Space - O(1)
*/
type Codec struct {
}

// Encodes a list of strings to a single string.
func (codec *Codec) Encode(strs []string) string {
    var ans string
    for _, str:=range strs {
        n:=len(str)
        ans+=fmt.Sprintf("%04d",n)
        ans+="#"
        ans+=str
    }
    return ans
}

// Decodes a single string to a list of strings.
func (codec *Codec) Decode(strs string) []string {
    res:=make([]string, 0)
    for i:=0;i<len(strs);i++ {
        n:=strs[i:i+4]
        nInt, _:=strconv.Atoi(n)
        i+=4
        i++
        res=append(res, strs[i:i+nInt])
        i+=nInt
        i--
    }
    return res
}

// Your Codec object will be instantiated and called as such:
// var codec Codec
// codec.Decode(codec.Encode(strs));