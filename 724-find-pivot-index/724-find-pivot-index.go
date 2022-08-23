func pivotIndex(nums []int) int {
    prefix:=make([]int, len(nums))
    suffix:=make([]int, len(nums))
    prefix[0]=nums[0]
    for i:=1;i<len(nums);i++ {
        prefix[i]=prefix[i-1]+nums[i]
    }
    suffix[len(nums)-1]=nums[len(nums)-1]
    for i:=len(nums)-2; i>=0;i-- {
        suffix[i]=suffix[i+1]+nums[i]
    }
    for i:=0;i<len(nums);i++ {
        if prefix[i]==suffix[i] {
            return i
        }
    }
    return -1
}