class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        freq=[0]*(max(nums)-min(nums)+1)
        offset=min(nums)
        for num in nums:
            freq[num-offset]+=1
        for i in range(len(freq)-1, -1, -1):
            if freq[i]!=0:
                k-=freq[i]
            if k<=0:
                return offset+i
        return -1
        
        
        
        