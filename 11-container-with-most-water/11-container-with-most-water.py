#Time - O(n)
#Space - O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        lo = 0
        hi = len(height)-1
        maxArea = 0
        while lo<hi:
            if height[lo]<height[hi]:
                area = height[lo]*(hi-lo)
                lo+=1
            else:
                area = height[hi]*(hi-lo)
                hi-=1
            if area>maxArea:
                maxArea=area
        return maxArea
                    
        