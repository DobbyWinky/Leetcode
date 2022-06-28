func twoSum(nums []int, target int) []int {
    sum:=make(map[int]int)
    for i:=0;i<len(nums);i++ {
        if val, ok:=sum[target-nums[i]]; ok {
            return []int{val, i}
        }
        sum[nums[i]]=i
    }
    return []int{-1,-1}
}