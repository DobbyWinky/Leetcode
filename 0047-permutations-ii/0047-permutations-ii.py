class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        n=len(nums)
        def helper(index):
            if index==n:
                ans.add(tuple(nums[:]))
            for i in range(index, n):
                nums[i], nums[index]=nums[index], nums[i]
                helper(index+1)
                nums[i], nums[index]=nums[index], nums[i]
        helper(0)
        return [list(ele) for ele in ans]
            
        