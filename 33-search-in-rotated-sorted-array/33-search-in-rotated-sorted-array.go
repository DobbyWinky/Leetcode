/*
Time - O(logn)
Space - O(1)
*/
func search(nums []int, target int) int {
    lo:=0
    hi:=len(nums)-1
    for lo<=hi {
        mid:=lo+(hi-lo)/2
        if nums[mid]==target {
            return mid
        }
        if nums[mid]>=nums[lo] {
            if target>nums[mid] {
                lo=mid+1
            }else if target<nums[lo] {
                lo=mid+1
            }else{
                hi=mid-1
            }
        }else {
            if target < nums[mid] {
                hi=mid-1
            }else if target>nums[hi] {
                    hi=mid-1
            }else {
                lo=mid+1
            }
        }
    }
    return -1
}