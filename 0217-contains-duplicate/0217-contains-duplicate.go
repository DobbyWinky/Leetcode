/*
Time - O(n)
Space - O(n)
*/
func containsDuplicate(nums []int) bool {
    dup:=make(map[int]bool)
    for _, num:=range nums {
        if dup[num]{
            return true
        }
        dup[num]=true
    }
    return false
}