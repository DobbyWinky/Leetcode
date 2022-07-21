func anagramMappings(nums1 []int, nums2 []int) []int {
    ans:=make([]int, len(nums1))
    hash:=make(map[int]int)
    for i:=0;i<len(nums2);i++ {
        hash[nums2[i]]=i
    }
    for i:=0;i<len(nums1);i++ {
        ans[i]=hash[nums1[i]]
    }
    return ans
}