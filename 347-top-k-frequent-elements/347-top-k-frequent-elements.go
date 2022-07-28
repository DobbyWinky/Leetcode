/*
N - number of elements
Time - O(N)
Space - O(N)
*/
func topKFrequent(nums []int, k int) []int {
    // Count the frequency of elements
    freq:=make(map[int]int)
    for _, num:=range nums {
        freq[num]++
    }
    // Bucket the elements based on their frequency
    count:=make([][]int, len(nums)+1)
    for k,v:=range freq {
        count[v]=append(count[v], k)
    }
    // Traverse from the last of the bucket and pick the last k elements which has the most frequency
    ans:=make([]int, 0)
    for i:=len(count)-1;i>=0 && k!=0 ;i-- {
        if len(count[i])!=0 {
            ans=append(ans, count[i]...)
            k-=len(count[i])
        }
    }
    return ans
}