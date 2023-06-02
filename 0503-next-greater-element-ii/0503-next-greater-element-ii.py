class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        n=len(nums)
        nge=[-1]*n
        for j in range(2*n-1, -1, -1):
            while len(stack)!=0 and stack[-1]<=nums[j%n]:
                stack.pop()
            if j<n:
                if len(stack)==0:
                    nge[j]=-1
                else:
                    nge[j]=stack[-1]
            stack.append(nums[j%n])
        return nge
                
            