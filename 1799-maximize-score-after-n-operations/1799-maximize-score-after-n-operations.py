class Solution:
    def maxScore(self, nums: List[int]) -> int:
        memo=collections.defaultdict(int)
        def dfs(mask, op):
            if mask in memo:
                return memo[mask]
            
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if (1<<i & mask) or (1<<j & mask):
                        continue
                    newMask=(1<<i | 1<<j | mask)
                    score=math.gcd(nums[i], nums[j])*op
                    memo[mask]=max(memo[mask], score+dfs(newMask, op+1))
            return memo[mask]
        
        return dfs(0, 1)