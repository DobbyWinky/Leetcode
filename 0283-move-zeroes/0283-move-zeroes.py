class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        i=0
        while i<n:
            if nums[i]==0:
                j=i
                while j<n and nums[j]==0:
                    j+=1
                if j<n:
                    nums[i], nums[j]=nums[j], nums[i]
            i+=1
        
        