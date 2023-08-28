class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash=collections.defaultdict(int)
        sum=0
        ans=0
        hash[0]=1
        for num in nums:
            sum+=num
            if sum-k in hash:
                ans+=hash[sum-k]
            hash[sum]+=1
        return ans
            
        