class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i in range(len(nums)):
            seen = set()
            for j in range(i+1, len(nums)):
                complement = -(nums[i]+nums[j])
                if complement in seen:
                    ans.add(tuple(sorted((nums[i], nums[j], complement))))  
                seen.add(nums[j])
        return list(ans)