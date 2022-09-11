func highFive(items [][]int) [][]int {
    avg:=make(map[int][]int)
    for i:=0;i<len(items);i++ {
        avg[items[i][0]]=append(avg[items[i][0]], items[i][1])
    }
    res:=make([][]int, 0)
    for k,v:=range avg {
        sort.Slice(v, func(i,j int) bool {
            return v[i]>v[j]
        })
        val:=make([]int,2)
        val[0]=k
        for i:=0;i<5;i++ {
            val[1]+=v[i]
        }
        val[1]/=5
        res=append(res, val)
    }
    sort.Slice(res, func(i,j int) bool {
        return res[i][0]<res[j][0]
    })
    return res
}