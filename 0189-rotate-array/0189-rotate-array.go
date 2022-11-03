/*
Time-O(n*k)
Space-O(1)
*/
func rotate(nums []int, k int)  {
    for i:=0;i<k;i++ {
        rotatedVal:=nums[len(nums)-1]
        prev:=nums[0]
        for i:=1;i<len(nums);i++ {
            curr:=nums[i]
            nums[i]=prev
            prev=curr
        }
        nums[0]=rotatedVal
    }
}