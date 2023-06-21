class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=[]
        vis=set()
        m=len(grid)
        n=len(grid[0])
        countRotten=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    countRotten+=1
                elif grid[i][j]==2:
                    queue.append((i,j))
                    vis.add((i,j))
        if countRotten==0:
            return 0
        time=0
        dir=[(1,0),(0,1),(-1,0),(0,-1)]
        while len(queue)>0:
            size=len(queue)
            if countRotten==0:
                    return time
            while size>0:
                x1,y1=queue.pop(0)
                for d in dir:
                    x=d[0]+x1
                    y=d[1]+y1
                    if x>=0 and x<m and y>=0 and y<n and (x,y) not in vis and grid[x][y]==1:
                        countRotten-=1
                        vis.add((x,y))
                        queue.append((x,y))
                size-=1
            time+=1
        if countRotten!=0:
            return -1
        return time
                    
                    