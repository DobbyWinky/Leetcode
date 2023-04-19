class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            res=helper(x, n//2)
            res=res*res
            return res if n%2==0 else x*res
            
        ans=helper(x, abs(n))
        return ans if n>=0 else 1/ans
        