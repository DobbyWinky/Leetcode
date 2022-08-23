func pivotIndex(nums []int) int {
    suffix:=make([]int, len(nums))
    suffix[len(nums)-1]=nums[len(nums)-1]
    for i:=len(nums)-2; i>=0;i-- {
        suffix[i]=suffix[i+1]+nums[i]
    }
    curr:=0
    for i:=0;i<len(nums);i++ {
        curr+=nums[i]
        if curr==suffix[i] {
            return i
        }
    }
    return -1
}