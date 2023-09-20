class Solution:
    def minSteps(self, s: str, t: str) -> int:
        t1=collections.defaultdict(int)
        t2=collections.defaultdict(int)
        for w in s:
            t1[w]+=1
            t2[w]=0
        for w in t:
            t2[w]+=1
            if w not in t1:
                t1[w]=0
        ans=0
        for k in t1:
            ans+=abs(t1[k]-t2[k])
        return ans//2
            
        
            
        