class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans=[]
        if n%2!=0:
            ans.append(0)
            n-=1
        for i in range(1, n//2+1):
            ans.append(i)
            ans.append(-i)
        return ans