/*
Time - O(n)
Space - O(n)
*/
func twoSum(nums []int, target int) []int {
    m:=make(map[int]int)
    ans:=make([]int, 0)
    for i, num:=range nums {
        if val, ok:=m[target-num]; ok {
            ans=append(ans, val)
            ans=append(ans, i)
            return ans
        }
        m[num]=i
    }
    return nil
}