/*
Time - O(n)
Space - O(1)
*/
func rotate(nums []int, k int)  {
    k=k%len(nums)
    reverse(nums)
    reverse(nums[:k])
    reverse(nums[k:])
}
func reverse(nums []int) {
    i:=0
    j:=len(nums)-1
    for i<=j {
        nums[i], nums[j]=nums[j], nums[i]
        i++
        j--
    }
}