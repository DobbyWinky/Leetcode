class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=set()
        ansList=[]
        for i in range(n):
            hash=set()
            for j in range(i+1, n):
                if -(nums[i]+nums[j]) in hash:
                    ans.add(tuple(sorted((nums[i], nums[j], -(nums[i]+nums[j])))))
                else:
                    hash.add(nums[j])
        for k in ans:
            ansList.append(k)
        return ansList
            
        