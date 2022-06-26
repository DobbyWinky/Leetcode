func rotate(nums []int, k int)  {
    n:=len(nums)
    r:=k%n
    last:=nums[n-r:]
    first:=nums[:n-r]
    temp:=append(last, first...)
    copy(nums, temp)
}