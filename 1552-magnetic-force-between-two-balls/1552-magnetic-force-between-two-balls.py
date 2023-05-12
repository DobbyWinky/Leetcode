class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def possible(mid):
            count=1
            pos=position[0]
            for i in range(1,len(position)):
                if position[i]-pos>=mid:
                    count+=1
                    pos=position[i]
                if count>=m:
                    return True
            return False
                
        lo=1
        hi=position[-1]-position[0]
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if possible(mid):
                lo=mid+1
            else:
                hi=mid-1
        return hi
        