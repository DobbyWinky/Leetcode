class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[[0 for _ in range(n)] for _ in range(n)]
        ans=""
        for i in range(n):
            dp[i][i]=1
            ans=s[i]
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=1
                ans=s[i:i+2]
        for j in range(2, n):
            for i in range(n):
                if i+j<n and s[i]==s[i+j] and dp[i+1][i+j-1]:
                    dp[i][i+j]=1
                    curr=s[i:i+j+1]
                    if len(curr)>len(ans):
                        ans=curr      
        return ans
                
        