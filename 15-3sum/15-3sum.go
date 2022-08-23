/*
Time - O(n2)
Space - O(n)
*/
func threeSum(nums []int) [][]int {
    ans:=make([][]int, 0)
    n:=len(nums)
    freq:=make(map[int]int)
    for i, num:=range nums {
        freq[num]=i
    }
    resMap:=make(map[[3]int]bool)
    for i:=0;i<n;i++ {
        for j:=i+1;j<n;j++ {
            complement:=-(nums[i]+nums[j])
            if val,ok:=freq[complement] ; ok && val!=i && val!=j {
                val:=[]int{nums[i], nums[j], complement}
                sort.Ints(val)
                if !resMap[[3]int{val[0], val[1], val[2]}] {
                    ans=append(ans, []int{nums[i], nums[j], complement})
                }
                resMap[[3]int{val[0], val[1], val[2]}]=true
            }
        }
    }
    return ans
}