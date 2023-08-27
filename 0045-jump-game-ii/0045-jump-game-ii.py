class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*n
        for i in range(n):
            for j in range(1, nums[i]+1):
                if i+j<n:
                    if dp[i+j]==0:
                        dp[i+j]=1+dp[i]
                    else:
                        dp[i+j]=min(dp[i+j], 1+dp[i])
        return dp[n-1]
        