func numIslands(grid [][]byte) int {
    m:=len(grid)
    n:=len(grid[0])
    visited:=make(map[[2]int]bool)
    var dfs func(i,j int) bool 
    dfs = func(i,j int) bool {
        if i<0 || i>=m || j<0 || j>=n || visited[[2]int{i,j}]==true || grid[i][j]=='0' {
            return false
        }
        visited[[2]int{i,j}]=true
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j-1)
        dfs(i, j+1)
        return true
    }
    count:=0;
    for i:=0;i<m;i++ {
        for j:=0;j<n;j++ {
            if !visited[[2]int{i,j}] && grid[i][j]=='1'&& dfs(i,j) {
                count++;
            }
        }
    }
    return count
}