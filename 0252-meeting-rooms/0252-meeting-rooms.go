func canAttendMeetings(intervals [][]int) bool {
    sort.Slice(intervals, func(i,j int)bool {
        if intervals[i][0]<intervals[j][0] {
            return true
        }
        return false
    })
    for i:=1;i<len(intervals);i++ {
        if intervals[i][0]<intervals[i-1][1] {
            return false
        }
    }
    return true
}