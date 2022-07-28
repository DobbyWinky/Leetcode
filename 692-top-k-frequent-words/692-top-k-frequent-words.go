/*
Time - O(NlogN)
Space - O(N)
*/
func topKFrequent(words []string, k int) []string {
    freq:=make(map[string]int)
    for _, word:=range words {
        freq[word]++
    }
    bucket:=make([][]string, len(words)+1)
    for k,v:=range freq {
        bucket[v]=append(bucket[v], k)
    }
    ans:=make([]string, 0)
    for i:=len(bucket)-1;i>=0&&k>0;i-- {
        if len(bucket[i])!=0 {
            sort.Strings(bucket[i])
            if k>=len(bucket[i]) {
                ans=append(ans, bucket[i]...)
            }else {
                ans=append(ans, bucket[i][:k]...)
            }
            k-=len(bucket[i])
        }
    }
    return ans
}