/*
Time - O(n)
Space - O(n)
*/
func productExceptSelf(nums []int) []int {
    prefix:=make([]int, len(nums))
    suffix:=make([]int, len(nums)) 
    prefix[0]=nums[0]
    for i:=1;i<len(nums);i++ {
        prefix[i]=prefix[i-1]*nums[i]
    }
    suffix[len(suffix)-1]=nums[len(nums)-1]
    for i:=len(nums)-2;i>=0;i-- {
        suffix[i]=suffix[i+1]*nums[i]
    }
    fmt.Println(prefix)
    fmt.Println(suffix)
    
    for i:=0;i<len(nums);i++ {
        var prev int
        var next int
        if i==0 {
            prev=1
        }else {
            prev=prefix[i-1]
        }
        if i==len(nums)-1 {
            next=1
        }else {
            next=suffix[i+1]
        }
        nums[i]=prev*next
    }
    return nums
}