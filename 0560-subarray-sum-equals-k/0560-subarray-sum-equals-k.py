# [1,1,-1,1] k=0 -> 2
# Step1: Compute the prefix sum at each point
# Step2: Check if arr[i]-k is in the hash if it is present count+=hash[arr[i]-k] -> arr[i]-x=k -> x=arr[i]-k
# Prefix sum {0:1, 1:2, 2:2} -> count=2
# [1, 3, 4, 7, -3, 3, -3, 3] k = 7 count=4 {0:1, 1:1, 4:1, 8:1, 15:3, 12:2, }  
# [1,1,1] k=2 count=2 , {0:1, 1:1, 2:1, 3:1}
# [1,-1,0] k=0 count=2 {0:3, 1:1, }
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=collections.defaultdict(int)
        prefix[0]=1
        count=0
        sum=0
        for num in nums:
            sum+=num
            if sum-k in prefix:
                count+=prefix[sum-k]
            prefix[sum]+=1
        return count
        