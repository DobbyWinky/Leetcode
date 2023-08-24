class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[n]=True
        i=n-1
        while i>=0:
            for word in wordDict:
                if i+len(word)<=n and word==s[i:i+len(word)] and dp[i+len(word)]:
                    dp[i]=True
                    break
            i-=1
        return dp[0]
            