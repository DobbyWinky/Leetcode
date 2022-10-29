func isInterleave(s1 string, s2 string, s3 string) bool {
    dp:=make(map[[2]int]bool)
    
    var dfs func(i,j int)bool 
    dfs=func(i,j int) bool{
        if i==len(s1) && j==len(s2) {
            return true
        }
        if val, ok:=dp[[2]int{i,j}]; ok {
            return val
        }
        if i<len(s1) && s3[i+j]==s1[i] && dfs(i+1,j) {
            dp[[2]int{i,j}]=true
            return true
        }
        if j<len(s2) && s3[i+j]==s2[j] && dfs(i, j+1) {
            dp[[2]int{i,j}]=true
            return true
        }
        dp[[2]int{i,j}]=false
        return false
    }
    if len(s1)+len(s2)!=len(s3) {
        return false
    }
    return dfs(0,0)
}