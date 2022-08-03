func highFive(items [][]int) [][]int {
    hash:=make(map[int][]int)
    for _, item:=range items {
        hash[item[0]]=append(hash[item[0]], item[1])
    }
    ans:=make([][]int, 0)
    sortedList:=make([]int, 0)
    for k,_:=range hash {
        sortedList=append(sortedList, k)
    }
    sort.Ints(sortedList)
    for _, sl:=range sortedList {
        sort.Ints(hash[sl])
        v:=hash[sl]
        avg:=0
        for i:=0;i<5;i++ {
            avg+=v[len(v)-i-1]
        }
        ans=append(ans, []int{sl,avg/5})
    }
    return ans
}