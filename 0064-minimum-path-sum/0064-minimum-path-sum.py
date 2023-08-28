class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[0 for _ in range(m)] for _ in range(n)]
        dp[0][0]=grid[0][0]
        for i in range(n):
            for j in range(m):
                if not (i==0 and j==0):
                    up=dp[i-1][j] if i-1>=0 else float('inf')
                    left=dp[i][j-1] if j-1>=0 else float('inf')
                    dp[i][j]=grid[i][j]+min(up, left)
        return dp[n-1][m-1]
        