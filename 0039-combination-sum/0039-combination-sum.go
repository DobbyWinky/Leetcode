func combinationSum(candidates []int, target int) [][]int {
    res:=make([][]int, 0)
    var dfs func(start, index int, curr []int) 
    dfs = func(start, index int, curr []int){
        if start==target {
            currCopy:=make([]int, len(curr))
            copy(currCopy, curr)
            res=append(res, currCopy)
            return
        }
        if start>target {
            return
        }
        for i:=index;i<len(candidates);i++ {
            curr=append(curr, candidates[i])
            dfs(start+candidates[i], i, curr)
            curr=curr[:len(curr)-1]
        }
    }
    curr:=make([]int, 0)
    dfs(0,0,curr)
    return res
}