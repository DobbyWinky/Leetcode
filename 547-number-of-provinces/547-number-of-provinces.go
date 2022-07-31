/*
Time - O(N2)
Space - O(N)
*/
func findCircleNum(isConnected [][]int) int {
    n:=len(isConnected)
    rank:=make([]int, n)
    root:=make([]int, n)
    // Initialize rank and root arrays
    for i:=0;i<n;i++ {
        rank[i]=1
        root[i]=i
    }
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
    for i:=0;i<n;i++ {
        for j:=0;j<n;j++ {
            if isConnected[i][j]==1 {
                if union(i,j) {
                    count--
                }
            }
        }
    }
    return count
}