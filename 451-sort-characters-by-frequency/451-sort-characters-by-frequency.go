/*
N is the length of string
K is the freq of each char
Q is the number of char with same freq
Time - O(N*K*Q)
Space - O(N)
*/
func frequencySort(s string) string {
    freq:=make(map[byte]int)
    for i:=0;i<len(s);i++ {
        freq[s[i]]++
    }
    bucket:=make([][]byte, len(s)+1)
    for k, v:=range freq {
        bucket[v]=append(bucket[v], k)
    }
    var ans []byte
    for i:=len(bucket)-1;i>=0;i-- {
        for j:=0;j<len(bucket[i]);j++ {
            for k:=0;k<i;k++ {
                ans=append(ans, bucket[i][j])
            }
        }
    }
    return string(ans)
}