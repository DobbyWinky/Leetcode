/*
Time: O(n)
Space: O(n)
*/
func sortColors(nums []int)  {
    count:=make(map[int]int)
    for _, num:=range nums {
        count[num]++
    }
    p:=0
    for i:=0;i<3;i++ {
        for count[i]!=0 {
            nums[p]=i
            p++
            count[i]--
        }
    }
}