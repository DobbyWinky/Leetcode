class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def helper(idx, curr):
            temp=curr[:]
            ans.append(temp)
            for i in range(idx, len(nums)):
                if i!=idx and nums[i-1]==nums[i]:
                    continue
                curr.append(nums[i])
                helper(i+1, curr)
                curr.pop()
        helper(0, [])
        return ans
        