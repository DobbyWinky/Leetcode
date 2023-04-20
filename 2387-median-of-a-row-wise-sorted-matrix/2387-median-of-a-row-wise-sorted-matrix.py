class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        lo=0
        hi=1e9
        m=len(grid)
        n=len(grid[0])
        def elementsGreaterThanOrEqual(row,target):
            lo=0
            hi=n-1
            while lo<=hi:
                mid=lo+(hi-lo)//2
                if grid[row][mid]<=target:
                    lo=mid+1
                else:
                    hi=mid-1
            return lo
        while lo<=hi:
            mid=lo+(hi-lo)//2
            count=0
            for i in range(m):
                count+=elementsGreaterThanOrEqual(i,mid)
            if count>(m*n//2):
                hi=mid-1
            else:
                lo=mid+1
        return int(lo)
        