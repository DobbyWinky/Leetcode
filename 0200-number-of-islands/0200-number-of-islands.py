class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        count=0
        vis=set()
        def dfs(r,c):
            if r>=m or r<0 or c>=n or c<0 or grid[r][c]=='0':
                return False
            if (r,c) in vis:
                return False
            vis.add((r,c))
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1, c)
            dfs(r, c-1)
            return True
        for i in range(m):
            for j in range(n):
                if dfs(i,j):
                    count+=1
        return count