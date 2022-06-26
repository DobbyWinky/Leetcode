func containsDuplicate(nums []int) bool {
    m:=make(map[int]bool)
    for _, num:=range nums {
        if m[num] {
            return true
        }
        m[num]=true
    }
    return false
}
