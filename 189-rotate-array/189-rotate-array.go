func rotate(nums []int, k int)  {
    n:=len(nums)
    r:=k%n
    temp:=append(nums[n-r:], nums[:n-r]...)
    copy(nums, temp)
}