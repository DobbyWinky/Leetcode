func minMovesToSeat(seats []int, students []int) int {
    sort.Ints(seats)
    sort.Ints(students)
    ans:=0
    for i:=0;i<len(seats);i++ {
        if seats[i]!=students[i] {
            ans+=abs(seats[i]-students[i])
        }
    }
    return ans
}

func abs(i int) int {
    if i<0 {
        return -i
    }
    return i
}