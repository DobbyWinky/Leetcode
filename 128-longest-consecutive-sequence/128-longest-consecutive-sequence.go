func longestConsecutive(nums []int) int {
    if len(nums)==0 {
        return 0
    }
    sort.Ints(nums)
    max:=1
    for i:=0;i<len(nums)-1;i++ {
        ans:=1
        for i<len(nums)-1 {
            if nums[i]==nums[i+1] {
                i++
            }else if nums[i]==nums[i+1]-1{
                i++
                ans++
            } else {
                break
            }
        }
        if ans>max {
            max=ans
        }
    }
    return max
}