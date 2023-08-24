class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeroPos=0
        n=len(nums)
        for i in range(n):
            if nums[i]!=0:
                nums[i], nums[zeroPos]=nums[zeroPos], nums[i]
                zeroPos+=1

        
        