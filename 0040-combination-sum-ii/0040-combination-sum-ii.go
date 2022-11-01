func combinationSum2(candidates []int, target int) [][]int {
    sort.Ints(candidates)
    res:=make([][]int, 0)
    var dfs func(start, index int, curr []int) 
    dfs = func(start, index int, curr []int){
        if start==target {
            currCopy:=make([]int, len(curr))
            copy(currCopy, curr)
            res=append(res, currCopy)
        }
        if start>target {
            return
        }
        prev:=-1
        for i:=index;i<len(candidates);i++ {
            if prev==candidates[i]{
                continue
            }
            curr=append(curr, candidates[i])
            dfs(start+candidates[i], i+1, curr)
            curr=curr[:len(curr)-1]
            prev=candidates[i]
        }
    }
    curr:=make([]int, 0)
    dfs(0,0,curr)
    return res
}