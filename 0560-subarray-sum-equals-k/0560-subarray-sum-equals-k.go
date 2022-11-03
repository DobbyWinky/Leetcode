/*
Time - O(n)
Space - O(n)
*/
func subarraySum(nums []int, k int) int {
    hash:=make(map[int]int)
    sum:=0
    ans:=0
    hash[0]=1
    for i:=0;i<len(nums);i++ {
        sum+=nums[i]
        if val, ok:=hash[sum-k];ok {
            ans+=val
        }
        hash[sum]++
    }
    return ans
}