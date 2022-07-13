/*
Time - O(n)
Space - O(n)
*/
func longestConsecutive(nums []int) int {
    if len(nums)==0 {
        return 0
    }
    hash:=make(map[int]bool)
    for _, num:=range nums {
        hash[num]=true
    }
    max:=1
    for k, _:=range hash {
        if !hash[k-1] {
            start:=k
            ans:=1
            for hash[start+1] {
                ans++
                start++
            }
            if ans>max {
                max=ans
            }
        }
    }
    return max
}