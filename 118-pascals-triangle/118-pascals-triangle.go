/*
Time - O(numRows^2)
Space - O(1)
*/
func generate(numRows int) [][]int {
    dp:=make([][]int, numRows)
    for i:=0;i<numRows;i++ {
        dp[i]=make([]int, i+1)
    }
    for i:=0;i<numRows;i++ {
        for j:=0;j<=i;j++ {
            if j==0 || i==j {
                dp[i][j]=1
            }else{
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
            }
        }
    }
    return dp
}