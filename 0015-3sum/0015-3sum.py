#Time: O(n2)
#Space: O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        for i in range (len(nums)):
            hash=set()
            for j in range (i+1, len(nums)):
                if -(nums[i]+nums[j]) in hash:
                    ans.add(tuple(sorted((nums[i], nums[j], -(nums[i]+nums[j])))))
                else:
                    hash.add(nums[j])
        return [elem for elem in ans]
        