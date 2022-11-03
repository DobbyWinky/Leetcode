/*
Time - O(n)
Space - O(n)
*/
func longestConsecutive(nums []int) int {
    if len(nums)==0 {
        return 0
    }
    hash:=make(map[int]bool)
    for i:=0;i<len(nums);i++ {
        hash[nums[i]]=true
    }
    maxStreak:=1
    i:=0
    for i<len(nums) {
        streak:=1
        val:=nums[i]
        if !hash[val-1]{
            for hash[val+1] {
                streak++
                val++
            }
            if streak>maxStreak {
                maxStreak=streak
            }
        }
        i++
    }
    return maxStreak
}