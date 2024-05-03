class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        dups=set()
        hash=collections.defaultdict(int)
        
        n=len(nums)
        for i in range(n):
            if nums[i] not in dups:
                dups.add(nums[i])
                for j in range(i+1, n):
                    if -(nums[i]+nums[j]) in hash and hash[-(nums[i]+nums[j])]!=i and hash[-(nums[i]+nums[j])]!=j:
                        ans.add(tuple(sorted((nums[i], nums[j], -(nums[i]+nums[j])))))
                    hash[nums[j]]=j
        return ans
                