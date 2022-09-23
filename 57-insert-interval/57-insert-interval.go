/*
Time - O(n)
Space - O(n)
*/
func insert(intervals [][]int, newInterval []int) [][]int {
    res:=make([][]int, 0)
    for i:=0;i<len(intervals);i++ {
        if newInterval[1]<intervals[i][0] {
            res=append(res, newInterval)
            res=append(res, intervals[i:]...)
            return res
        }else if newInterval[0]<=intervals[i][1] {
            newInterval[0]=min(newInterval[0], intervals[i][0])
            newInterval[1]=max(newInterval[1], intervals[i][1])
        }else {
            res=append(res, intervals[i])
        }
    }
    res=append(res, newInterval)
    
    return res
}

func min(i, j int) int {
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