func findMin(nums []int) int {
    lo:=0
    hi:=len(nums)-1
    if nums[lo]<nums[hi] {
        return nums[lo]
    }
    for lo<hi{
        mid:=lo+(hi-lo)/2
        if nums[mid]>nums[mid+1] {
            return nums[mid+1]
        }
        if nums[mid-1]>nums[mid] {
            return nums[mid]
        }
        if nums[mid]>nums[0] {
            lo=mid+1
        }else {
            hi=mid-1
        }
    }
    return nums[lo]
}