/*
No sort algo
Time - O(n2)
Space - O(n)
*/
func threeSum(nums []int) [][]int {
    res:=make(map[[3]int]bool)
    for i:=0;i<len(nums);i++ {
        seen:=make(map[int]bool)
        for j:=i+1;j<len(nums);j++ {
            // Check for duplicates and chexk if the compliment exists in the hash map
            // If the compliment exists, put the result into a map to avoid duplicates in the result
            if seen[-(nums[i]+nums[j])] {
                temp:=[]int{nums[i],nums[j],-(nums[i]+nums[j])}
                // This sorting was required since the leetcode solution was expected to be sorted. This sorting takes O(1) since it sorts only 3 elements at a given point of time
                sort.Ints(temp)
                res[[3]int{temp[0],temp[1],temp[2]}]=true
            }
            seen[nums[j]]=true
        } 
    }
    
    // Convert the map answer constructed in the previous steps to a slice which is expected by the leetcode solution
    ans:=make([][]int, 0)
    for k,_:=range res {
        ans=append(ans, []int{k[0],k[1],k[2]})
    }
    return ans
}