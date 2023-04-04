class Solution:
            
    def solveNQueens(self, n: int) -> List[List[str]]:  
        def isSafe(row, col, board):
            n=len(board)
            duprow=row
            dupcol=col
            while col>=0 and row>=0:
                if board[row][col]=='Q':
                    return False
                row-=1
                col-=1
            row=duprow
            col=dupcol
            while col>=0:
                if board[row][col]=='Q':
                    return False
                col-=1
            row=duprow
            col=dupcol   
            while row<n and col>=0:
                if board[row][col]=='Q':
                    return False
                row+=1
                col-=1
            return True
    
        board=[]
        for i in range(n):
            s=[]
            for j in range(n):
                s.append('.')
            board.append(s)
        
        ans=[]
        def helper(col, board):
            if col==n:
                temp=[]
                for row in range(len(board)):
                    temp.append("".join(board[row]))
                ans.append(temp)
                return
            for row in range(n):
                if isSafe(row, col, board):
                    board[row][col]='Q'
                    helper(col+1, board)
                    board[row][col]='.'
        helper(0, board)
        return ans
        
                
        