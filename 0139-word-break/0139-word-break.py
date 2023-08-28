class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[n]=True
        for i in range(n-1, -1, -1):
            for word in wordDict:
                if i+len(word)<=n and dp[i+len(word)] and s[i:i+len(word)]==word:
                    dp[i]=True
        return dp[0]
                    
        