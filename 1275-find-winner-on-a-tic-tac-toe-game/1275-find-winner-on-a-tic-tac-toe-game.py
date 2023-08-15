class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def checkWin(moves):
            for row in range(3):
                first=grid[row][0]
                win=True
                for j in range(1,3):
                    if grid[row][j]!=first:
                        win=False
                        break
                if win:
                    return first
            
            for col in range(3):
                first=grid[0][col]
                win=True
                for i in range(1,3):
                    if grid[i][col]!=first:
                        win=False
                        break
                if win:
                    return first
            first=grid[0][0]
            win=True
            for i in range(1,3):
                if grid[i][i]!=first:
                    win=False
                    break
            if win:
                return first
            
            win=True
            first=grid[0][2]
            for i in range(2,-1,-1):
                if grid[2-i][i]!=first:
                    win=False
                    break
            if win:
                return first
            for i in range(3):
                for j in range(3):
                    if grid[i][j]=='.':
                        return "Pending"
            return "Draw"
      
        n=len(moves)
        grid=[['.' for _ in range(3)] for _ in range(3)]
        for i in range(n):
            if i%2==0:
                grid[moves[i][0]][moves[i][1]]='A'
            else:
                grid[moves[i][0]][moves[i][1]]='B'
        ans=checkWin(grid)
        if ans=='.':
            return "Pending"
        return ans
    
            
            