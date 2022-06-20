func removeDuplicates(nums []int) int {
    k:=0
    i:=0
    j:=0
    for j<len(nums) {
        if nums[i]!=nums[j] {
            nums[k+1]=nums[j]
            i=j
            k++
        }
        j++
    }
    return k+1
}