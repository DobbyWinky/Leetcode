/*
Time - O(N)
Space - O(N)
*/
func earliestAcq(logs [][]int, n int) int {
    m:=len(logs)
    rank:=make([]int, n)
    root:=make([]int, n)
    // Initialize rank and root arrays
    for i:=0;i<n;i++ {
        rank[i]=1
        root[i]=i
    }
    sort.Slice(logs, func(i,j int) bool {
        return logs[i][0]<logs[j][0]
    })
    var find func(x int) int
    find = func(x int) int{
        for x!=root[x] {
            x=root[x]
        }
        return x
    }
    var union func(i,j int) bool
    union = func(i,j int) bool {
        rootx:=find(i)
        rooty:=find(j)
        if rootx!=rooty {
            if rank[rootx]>rank[rooty] {
                root[rooty]=rootx
                rank[rootx]+=1
            }else {
                root[rootx]=rooty
                rank[rooty]+=1
            }
            return true
        }
        return false
    }
    count:=n
    for i:=0;i<m;i++ {
        if union(logs[i][1],logs[i][2]) {
            count--
            if count==1 {
                return logs[i][0]
            }
        }
    }
    return -1
}
