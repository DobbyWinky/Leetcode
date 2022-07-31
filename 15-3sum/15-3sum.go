/*
Time - O(n^2)
Space - O(n^2)
*/
func threeSum(nums []int) [][]int {
    ans:=make(map[[3]int]bool)
    for i:=0;i<len(nums);i++ {
        seen:=make(map[int]int)
        for j:=i+1;j<len(nums);j++ {
            if _, ok:=seen[-(nums[j]+nums[i])]; ok {
                res:=[]int{nums[i],nums[j],-(nums[j]+nums[i])}
                sort.Ints(res)         
                ans[[3]int{res[0],res[1],res[2]}]=true
            }
            seen[nums[j]]=j
        }
    }
    ansFinal:=make([][]int, 0)
    for k,_:=range ans {
        ansFinal=append(ansFinal, []int{k[0],k[1],k[2]})
    }
    return ansFinal
}