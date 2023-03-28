class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def helper(idx, curr):
            temp=curr[:]
            ans.append(temp)
            for i in range(idx, len(nums)):
                curr.append(nums[i])
                helper(i+1, curr)
                curr.pop()
        helper(0, [])
        return ans
        