func moveZeroes(nums []int)  {
    ans:=make([]int, len(nums))
    p:=0
    for i:=0;i<len(nums);i++ {
        if nums[i]!=0 {
            ans[p]=nums[i]
            p++
        }
    }
    copy(nums, ans)
}