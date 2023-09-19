class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        lo=1
        hi=maxSum
        l=index
        r=n-index-1
        res=0
        while lo<=hi:
            mid=lo+(hi-lo)//2
            sum=mid
            m=mid-1
            lSum=0
            rSum=0
            if r<=m:
                rSum=m*(m+1)//2 - (m-r)*(m-r+1)//2
            else:
                rSum=m*(m+1)//2 + (r-m)*1
            if l<=m:
                lSum=m*(m+1)//2 - (m-l)*(m-l+1)//2
            else:
                lSum=m*(m+1)//2 + (l-m)*1
            
            sum+=lSum+rSum
            if sum<=maxSum:
                res=mid
                lo=mid+1
            else:
                hi=mid-1
        return res
            
        