class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash=collections.defaultdict(int)
        for i, num in enumerate(nums):
            if target-num in hash:
                return [i, hash[target-num]]
            hash[num]=i
        return []
        