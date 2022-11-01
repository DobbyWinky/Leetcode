/*
Time - O(n)
Space - O(n)
*/
func majorityElement(nums []int) int {
    freq:=make(map[int]int)
    max:=0
    maxEle:=0
    for i:=0;i<len(nums);i++ {
        freq[nums[i]]++
        if freq[nums[i]]>max {
            max=freq[nums[i]]
            maxEle=nums[i]
        }
    }
    return maxEle
}