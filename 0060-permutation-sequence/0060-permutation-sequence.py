class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums=[]
        fact=1
        for i in range(1,n):
            fact*=i
            nums.append(i)
        nums.append(n)
        ans=""
        k=k-1
        while True:
            ans+=str(nums[k//fact])
            nums.pop(k//fact)
            if len(nums)==0:
                break
            k=k%fact
            fact=fact//len(nums)
        return ans
        