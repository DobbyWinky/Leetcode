class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n=len(s)
        m=len(p)
        def dfs(i,j):
            if i>=n and j>=m:
                return True
            if j>=m:
                return False
            match = i<n and (s[i]==p[j] or p[j]=='.')
            if j+1<m and p[j+1]=='*':
                return dfs(i, j+2) or (match and dfs(i+1,j))
            if match:
                return dfs(i+1, j+1)
            return False
        return dfs(0,0)
        