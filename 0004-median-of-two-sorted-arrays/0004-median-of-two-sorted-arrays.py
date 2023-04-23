class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1=len(nums1)
        n2=len(nums2)
        if n1>n2:
            return self.findMedianSortedArrays(nums2, nums1)
        lo=0
        hi=n1
        while lo<=hi:
            cut1=lo+(hi-lo)//2
            cut2=(n1+n2+1)//2-cut1
            l1=nums1[cut1-1] if cut1!=0 else -2147483648
            l2=nums2[cut2-1] if cut2!=0 else -2147483648
            r1=nums1[cut1] if cut1<n1 else 2147483647
            r2=nums2[cut2] if cut2<n2 else 2147483647
            if l1<=r2 and l2<=r1:
                if (n1+n2)%2!=0:
                    return max(l1,l2)
                else:
                    return (max(l1,l2)+min(r1,r2))/2
            elif l1>r2:
                hi=cut1-1
            else:
                lo=cut1+1
        return -1
        