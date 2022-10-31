/*
Time - O(n^2)
Space - O(n)
*/
func threeSum(nums []int) [][]int {
    ans:=make([][]int, 0)
    temp:=make(map[[3]int]bool)
    for i:=0;i<len(nums);i++ {
        m:=make(map[int]int)
        target:=nums[i]
        for j:=0;j<len(nums)&&j!=i;j++ {
            if val, ok:=m[-(nums[j]+target)];ok&& val!=j {
                t:=[]int{-(nums[j]+target), nums[j], nums[i]}
                sort.Ints(t)
                temp[[3]int{t[0], t[1], t[2]}]=true
            }
            m[nums[j]]=j
        }
    }
    for k,_:=range temp {
        ans=append(ans, []int{k[0],k[1],k[2]})
    }
    return ans
}