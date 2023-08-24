class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        freq=collections.defaultdict(int)
        for num in nums:
            freq[num]+=1
        countArr=[[] for _ in range(n+1)]
        for p,v in freq.items():
            countArr[v].append(p)
        ans=[]
        for i in range(n, -1, -1):
            if k<=0:
                return ans
            if len(countArr[i])!=0:
                ans.extend(x for x in countArr[i])
                k-=len(countArr[i])
        return ans
            
        