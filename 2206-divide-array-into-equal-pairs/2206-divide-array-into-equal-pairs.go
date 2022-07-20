func divideArray(nums []int) bool {
    hash:=make(map[int]int)
    for i:=0;i<len(nums);i++ {
        hash[nums[i]]++
    }
    for _,v:=range hash {
        if v%2!=0 {
            return false
        }
    }
    return true
}