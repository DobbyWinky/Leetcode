class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        n=len(nums)
        for i in range(0, n, 2):
            ans+=nums[i]
        return ans
        