/*
Time -O(nlogn)
Space - O(n)
*/
func merge(intervals [][]int) [][]int {
    sort.Slice(intervals, func(i,j int)bool {
        if intervals[i][0]<intervals[j][0] {
            return true
        }
        return false
    })
    res:=make([][]int, 0)
    for i:=0;i<len(intervals);i++ {
        if len(res)==0 {
            res=append(res, intervals[i])
            continue
        }
        if intervals[i][0]<=res[len(res)-1][1] {
            res[len(res)-1][1]=max(res[len(res)-1][1], intervals[i][1])
        }else {
            res=append(res, intervals[i])
        }
    }
    return res
}

func max(i,j int) int {
    if i>j {
        return i
    }
    return j
}