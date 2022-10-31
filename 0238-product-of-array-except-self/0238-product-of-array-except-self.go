/*
Time - O(n)
Space - O(n)
*/

func productExceptSelf(nums []int) []int {
    prefix:=make([]int, len(nums))
    suffix:=make([]int, len(nums))
    prefix[0]=1
    prefix[1]=nums[0]
    for i:=2;i<len(nums);i++ {
        prefix[i]=nums[i-1]*prefix[i-1]
    }
    suffix[len(suffix)-1]=1
    suffix[len(suffix)-2]=nums[len(nums)-1]
    for j:=len(nums)-3;j>=0;j-- {
        suffix[j]=suffix[j+1]*nums[j+1]
    }
    for i:=0;i<len(prefix);i++ {
        prefix[i]*=suffix[i]
    }
    return prefix
}