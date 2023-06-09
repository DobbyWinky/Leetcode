class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        n=len(heights)
        leftSmall=[0]*n
        rightSmall=[n-1]*n
        for i,h in enumerate(heights):
            if len(stack)==0:
                stack.append(i)
                continue
            while len(stack)!=0 and heights[stack[-1]]>h:
                stack.pop()
            if len(stack)==0:
                leftSmall[i]=0
            else:
                leftSmall[i]=stack[-1]+1
            stack.append(i)
        stack.clear()
        for i in range(n-1,-1,-1):
            if len(stack)==0:
                stack.append(i)
                continue
            while len(stack)!=0 and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if len(stack)==0:
                rightSmall[i]=n-1
            else:
                rightSmall[i]=stack[-1]-1
            stack.append(i)
        maxArea=0
        for i in range(n):
            if (rightSmall[i]-leftSmall[i]+1)*heights[i]>maxArea:
                maxArea=(rightSmall[i]-leftSmall[i]+1)*heights[i]
        return maxArea
        