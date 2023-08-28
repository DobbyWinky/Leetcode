class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res=[]
        res.append([rStart,cStart])
        dirs=[(0,1),(1,0),(0,-1),(-1,0)]
        dir_idx=0
        increment=1
        total=rows*cols
        steps=1
        while len(res)<total:
            for i in range(increment):
                rStart=rStart+dirs[dir_idx][0]
                cStart=cStart+dirs[dir_idx][1]
                if rStart>=0 and rStart<rows and cStart>=0 and cStart<cols:
                    res.append([rStart, cStart])
            dir_idx=(dir_idx+1)%4
            if steps%2==0:
                increment+=1
            steps+=1
        return res
        
            
        
        