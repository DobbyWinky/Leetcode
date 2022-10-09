func generate(numRows int) [][]int {
    ans:=make([][]int, 0)
    for i:=1;i<=numRows;i++ {
        row:=make([]int, i)
        row[0]=1
        row[len(row)-1]=1
        for j:=1;j<i-1;j++ {
            row[j]=ans[i-2][j-1]+ans[i-2][j]
        }
        ans=append(ans, row)
    }
    return ans
}