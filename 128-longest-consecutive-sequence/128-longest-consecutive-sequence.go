/*
    Time - O(nlogn)
    Space - O(1)
*/
func longestConsecutive(nums []int) int {
    if len(nums)==1 {
        return 1
    }
    sort.Ints(nums)
    max:=0
    for i:=0;i<len(nums)-1;i++ {
        k:=1
        for i<len(nums)-1 {
            if nums[i]+1==nums[i+1] {
                k++
                i++
            }else if nums[i]==nums[i+1] {
                i++
            }else {
                break
            }
        }
        max=maximum(max, k)
    }
    return max
}

func maximum(i,j int) int {
    if i>j {
        return i
    }
    return j
}