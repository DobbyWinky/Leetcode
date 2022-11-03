/*
Time - O(n)
Space - O(n)
*/
func findMaxLength(nums []int) int {
    hash:=make(map[int]int)
    sum:=0
    longest:=0
    for i:=0;i<len(nums);i++ {
        if nums[i]==0 {
            sum--
        }else {
            sum++
        }
        if sum==0 {
            longest=i+1
            continue
        }
        if val, ok:= hash[sum]; ok {
            if i-val>longest {
                longest=i-val
            }
        }else {
            hash[sum]=i
        }
    }
    return longest
}