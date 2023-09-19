class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n=len(s)
        count=0
        
        @cache
        def dfs(i):
            if i==n:
                return 0
            count=1+dfs(i+1)
            for j in range(i,n):
                if s[i:j+1] in dictionary:
                    count=min(count, dfs(j+1))
            return count
        return dfs(0)
                    
        