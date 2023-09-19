class Solution:
    def soupServings(self, n: int) -> float:
        if n>5000:
            return 1
        memo=collections.defaultdict(int)
        def dfs(a,b):
            if (a,b) in memo:
                return memo[(a,b)]
            if a<=0 and b<=0:
                return 0.5
            if a<=0:
                return 1
            if b<=0:
                return 0
            memo[(a,b)]=1/4*(dfs(a-100,b)+dfs(a-75,b-25)+dfs(a-50,b-50)+dfs(a-25,b-75))
            return memo[(a,b)]
        
        return dfs(n,n)
        