/*
Time - O(n)
Space - O(1)
*/
func twoSum(nums []int, target int) []int {
    lo:=0
    hi:=len(nums)-1
    for lo<hi {
        if nums[lo]+nums[hi]==target {
            return []int{lo+1, hi+1}
        }
        if nums[lo]+nums[hi]<target {
            lo++
        }else {
            hi--
        }
    }
    return []int{-1,-1}
}