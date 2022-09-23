/*
Time - O(nlogn)
Space - O(1)
*/
func insert(intervals [][]int, newInterval []int) [][]int {
    intervals=append(intervals, newInterval)
    sort.Slice(intervals, func (i,j int) bool {
        return intervals[i][0]<intervals[j][0]
    })
    res:=make([][]int, 0)
    res=append(res, intervals[0])
    for i:=1;i<len(intervals);i++ {
        if intervals[i][0]<=res[len(res)-1][1] {
            res[len(res)-1][1]=max(res[len(res)-1][1], intervals[i][1])
        }else {
            res=append(res, intervals[i])
        }
    }
    return res
}

func max(i, j int) int {
    if i>j {
        return i
    }
    return j
}