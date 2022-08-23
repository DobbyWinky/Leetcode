/*
Time - O(n2)
Space - O(1)
*/
func twoSumLessThanK(nums []int, k int) int {
    n:=len(nums)
    maxSoFar:=0
    for i:=0;i<n;i++ {
        for j:=i+1;j<n;j++ {
            if nums[i]+nums[j]<k {
                if nums[i]+nums[j]>maxSoFar {
                    maxSoFar=nums[i]+nums[j]
                }
            }
        }
    }
    if maxSoFar!=0 {
        return maxSoFar
    }
    return -1
}