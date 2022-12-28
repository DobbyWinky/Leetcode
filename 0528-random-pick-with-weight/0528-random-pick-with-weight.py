class Solution:

    def __init__(self, w: List[int]):
        self.cumulative=[]
        self.curr=w
        total=0
        
        for i in w:
            total+=i
            self.cumulative.append(total)
        self.total=total
        
        
    def pickIndex(self) -> int:
        r=int(random.uniform(0,self.total))
        idx=bisect.bisect(self.cumulative,r)
        return idx
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()