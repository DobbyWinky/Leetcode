func intersect(nums1 []int, nums2 []int) []int {
    m:=make(map[int]int)
    for i:=0;i<len(nums1);i++ {
        m[nums1[i]]++
    }
    ans:=make([]int, 0)
    for i:=0;i<len(nums2);i++ {
        if m[nums2[i]]>0 {
            ans=append(ans, nums2[i])
            m[nums2[i]]--
        }
    }
    return ans
}