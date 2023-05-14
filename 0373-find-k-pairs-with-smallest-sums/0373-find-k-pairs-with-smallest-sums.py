class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap=[]
        ans=[]
        hash=set()
        n=len(nums1)
        m=len(nums2)
        heapq.heappush(heap, (nums1[0]+nums2[0],[0,0],[nums1[0],nums2[0]]))
        hash.add((0,0))
        while k>0 and len(heap)!=0:
            pop=heapq.heappop(heap)
            ans.append(pop[2])
            x=pop[1][0]
            y=pop[1][1]
            if (x+1,y) not in hash and x+1<n:
                heapq.heappush(heap, (nums1[x+1]+nums2[y],[x+1,y],[nums1[x+1], nums2[y]]))
                hash.add((x+1,y))
            if (x,y+1) not in hash and y+1<m:
                heapq.heappush(heap, (nums1[x]+nums2[y+1],[x,y+1],[nums1[x], nums2[y+1]]))
                hash.add((x,y+1))
            k-=1
        return ans
        