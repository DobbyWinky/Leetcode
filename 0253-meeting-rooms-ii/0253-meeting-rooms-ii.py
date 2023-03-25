class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start=[]
        end=[]
        for i in range(len(intervals)):
            start.append(intervals[i][0])
            end.append(intervals[i][1])
        start.sort()
        end.sort()
        
        curr=0
        maxRoom=1
        s=0
        e=0
        while s<len(start) and e<len(end):
            if start[s]<end[e]:
                s+=1
                curr+=1
                maxRoom=max(maxRoom, curr)
            else:
                e+=1
                curr-=1
        return maxRoom
            