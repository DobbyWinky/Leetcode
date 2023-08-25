class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        n=len(height)
        right=n-1
        maxArea=0
        while left<right:
            maxArea=max(maxArea, min(height[left], height[right])*(right-left))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxArea
            