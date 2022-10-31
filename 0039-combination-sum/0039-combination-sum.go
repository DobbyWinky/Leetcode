func combinationSum(candidates []int, target int) [][]int {
    res:=make([][]int, 0)
    var dfs func(i, start int, curr []int) 
    dfs=func(i, start int, curr []int) {
        if start==target {
            currCopy:=make([]int, len(curr))
            copy(currCopy, curr)
            res=append(res, currCopy)
            return 
        }
        if i>=len(candidates) || start>target {
            return
        }
        curr=append(curr, candidates[i])
        dfs(i, start+candidates[i], curr)
        curr=curr[:len(curr)-1]
        dfs(i+1, start, curr)
    }
    curr:=make([]int, 0)
    dfs(0,0,curr)
    return res
}