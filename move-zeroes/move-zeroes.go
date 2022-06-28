func moveZeroes(nums []int)  {
    zeroPos:=0
    for i:=0;i<len(nums);i++ {
        if nums[i]!=0 {
            nums[i], nums[zeroPos]=nums[zeroPos], nums[i]
            zeroPos++
        }
    }
}