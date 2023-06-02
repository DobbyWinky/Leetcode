class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        n2=len(nums2)
        hash=collections.defaultdict()
        for i, num in enumerate(nums1):
            hash[num]=i
        nge=[-1]*len(hash)
        
        for j in range(n2-1, -1, -1):
            while len(stack)!=0 and stack[-1]<=nums2[j]:
                stack.pop()
            if nums2[j] in hash:
                if len(stack)!=0:
                    nge[hash[nums2[j]]]=stack[-1]
            stack.append(nums2[j])
        return nge
        
            
        