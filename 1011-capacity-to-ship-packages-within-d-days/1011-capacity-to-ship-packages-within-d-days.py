class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isPossible(barrier):
            w=0
            currDay=1
            for i in range(len(weights)):
                if weights[i]>barrier:
                    return False
                if w+weights[i]>barrier:
                    w=weights[i]
                    currDay+=1
                else:
                    w+=weights[i]
            if currDay>days:
                return False
            return True
        
        lo=min(weights)
        hi=sum(weights)
        res=-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if isPossible(mid):
                res=mid
                hi=mid-1
            else:
                lo=mid+1    
        return lo
        