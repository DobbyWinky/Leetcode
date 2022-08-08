/*
Time - O(n2+nlogn)
Space - O(n) - Depending sorting algo
*/
func threeSum(nums []int) [][]int {
    sort.Ints(nums)
    ans:=make([][]int, 0)
    for i:=0;i<len(nums);i++ {
        target:=nums[i]
        if !(i==0 ||nums[i-1]!=nums[i]) {
            continue
        }
        lo:=i+1
        hi:=len(nums)-1
        for lo<hi {
            if nums[lo]+nums[hi]==-target {
                ans=append(ans, []int{target, nums[lo], nums[hi]})
                lo++
                hi--
                for lo<hi && nums[lo]==nums[lo-1] {
                    lo++
                }
            }else if nums[lo]+nums[hi]>-target {
                hi--
            }else {
                lo++
            }
        }
    }
    return ans
}