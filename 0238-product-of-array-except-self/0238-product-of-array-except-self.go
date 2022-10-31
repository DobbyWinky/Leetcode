/*
Time - O(n)
Space - O(1)
*/

func productExceptSelf(nums []int) []int {
    prefix:=make([]int, len(nums))
    prefix[0]=1
    prefix[1]=nums[0]
    for i:=2;i<len(nums);i++ {
        prefix[i]=nums[i-1]*prefix[i-1]
    }
    right:=1
    for j:=len(nums)-1;j>=0;j-- {
        prefix[j]*=right
        right*=nums[j]
    }
    return prefix
}