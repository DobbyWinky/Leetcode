/*
Time - O(n)
Space - O(1)
*/
func findDuplicates(nums []int) []int {
    res:=make([]int, 0)
    for _, num:=range nums {
        if nums[abs(num)-1]<0 {
            res=append(res, abs(num))
        }
        nums[abs(num)-1]*=-1
    }
    return res
}
func abs(i int) int {
    if i<0 {
        return -i
    }
    return i
}