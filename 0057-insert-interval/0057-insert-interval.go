/*
Time - O(n)
Space - O(n) -- For the extra output space
*/
func insert(intervals [][]int, newInterval []int) [][]int {
    // if len(intervals)==0 {
    //     return [][]int{newInterval}
    // }
    res:=make([][]int,0)
    // if newInterval[1]<intervals[0][0] {
    //     intervals=append([][]int{newInterval}, intervals...)
    //     return intervals
    // }
    for i:=0;i<len(intervals);i++ {
        if newInterval[1]<intervals[i][0] {
            res=append(res, newInterval)
            res=append(res, intervals[i:]...)
            return res
        }else if newInterval[0]<=intervals[i][1] {
            newInterval[0]=min(intervals[i][0], newInterval[0])
            newInterval[1]=max(intervals[i][1], newInterval[1])
        }else{
            res=append(res, intervals[i])
        }
    }
    res=append(res, newInterval)
    return res
}

func min(i,j int) int {
    if i<j {
        return i
    }
    return j
}

func max(i,j int) int {
    if i>j {
        return i
    }
    return j
}