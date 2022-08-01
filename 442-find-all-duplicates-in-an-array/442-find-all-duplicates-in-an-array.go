/*
Time - O(n)
Space - O(n)
*/
func findDuplicates(nums []int) []int {
    dup:=make([]int, 0)
    hash:=make(map[int]bool)
    for i:=0;i<len(nums);i++ {
        if hash[nums[i]] {
            dup=append(dup, nums[i])
        }
        hash[nums[i]]=true
    }
    return dup
}