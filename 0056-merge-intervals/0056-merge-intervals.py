class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[]
        res.append([intervals[0][0], intervals[0][1]])
        for i in range(1, len(intervals)):
            if res[-1][1]>=intervals[i][0]:
                res[-1][1]=max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        return res
                
        