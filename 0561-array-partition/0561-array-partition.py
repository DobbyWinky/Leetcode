class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        k=10000
        freq=[0]*(2*k+1)
        for num in nums:
            freq[num+k]+=1
        is_even=True
        ans=0
        for i in range(2*k+1):
            while freq[i]>0:
                if is_even:
                    ans+=i-k
                is_even=not is_even
                freq[i]-=1
        return ans
        