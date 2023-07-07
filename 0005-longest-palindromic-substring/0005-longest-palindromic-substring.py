class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        maxLen=1
        left=-1
        right=-1
        ans=""
        dp=[[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i]=1
            ans=s[i]
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=1
                maxLen=2
                ans=s[i:i+2]
        for d in range(2,n):
            for i in range(n):
                j=d+i
                if j<n and s[i]==s[j] and i+1<n and j-1>=0 and dp[i+1][j-1]:
                    dp[i][j]=1
                    if (j-i+1)>maxLen:
                        maxLen=j-i+1
                        left=i
                        right=j
        if left!=-1 and right!=-1:
            ans=s[left:right+1]
        return ans
        
        