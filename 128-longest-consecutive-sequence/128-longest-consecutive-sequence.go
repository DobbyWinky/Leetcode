/*
    Time - O(n)
    Space - O(1)
*/
func longestConsecutive(nums []int) int {
    hash:=make(map[int]bool)
    for i:=0;i<len(nums);i++ {
        hash[nums[i]]=true
    }
    max:=0
    for i:=0;i<len(nums);i++ {
        if !hash[nums[i]-1] {
            curr:=nums[i]
            k:=1
            for hash[curr+1] {
                curr=curr+1
                k++
            }
            max=maximum(max, k)
        }
    }
    return max
}
func maximum(i,j int) int {
    if i>j {
        return i
    }
    return j
}