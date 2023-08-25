class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n=len(s)
        m=len(p)
        memo={}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i>=n and j>=m:
                return True
            if j>=m:
                return False
            match = i<n and (s[i]==p[j] or p[j]=='.')
            if j+1<m and p[j+1]=='*':
                memo[(i,j)]=dfs(i, j+2) or (match and dfs(i+1,j))
                return memo[(i,j)]
            if match:
                memo[(i,j)]=dfs(i+1, j+1)
                return memo[(i,j)]
            memo[(i,j)]=False
            return False
        return dfs(0,0)
        