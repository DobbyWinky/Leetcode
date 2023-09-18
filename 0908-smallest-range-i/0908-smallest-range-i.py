class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        if nums[0]+k>=nums[-1]-k:
            return 0
        else:
            return abs(nums[0]+k-(nums[-1]-k))
        