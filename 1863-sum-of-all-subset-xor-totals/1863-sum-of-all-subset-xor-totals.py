class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans=0
        for num in nums:
            ans+=num
        for i in range(2, len(nums)+1):
            for k in list(itertools.combinations(nums, i)):
                xor=0
                for p in range(len(k)):
                    xor^=k[p]
                ans+=xor
        return ans
                
        