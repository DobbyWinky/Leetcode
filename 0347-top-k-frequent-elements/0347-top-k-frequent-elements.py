class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=collections.defaultdict(int)
        for num in nums:
            freq[num]+=1
        
        count=[[] for i in range(len(nums)+1)]
        
        for key in freq:
            count[freq[key]].append(key)
            
        ans=[]
        
        for i in range(len(count)-1, 0, -1):
            for n in count[i]:
                ans.append(n)
            k-=len(count[i])
            if k<=0:
                return ans
        return None
        