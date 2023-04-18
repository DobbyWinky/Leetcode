#User function Template for python3

class Solution:
    def findPath(self, mat, n):
        if mat[n-1][n-1]==0:
            return []
        ans=[]
        vis=set()
        def helper(r,c, curr):
            if r==n-1 and c==n-1:
                ans.append(curr)
                return
            if r<0 or c<0 or r>=n or c>=n or mat[r][c]==0:
                return
            if (r,c) in vis:
                return
            vis.add((r,c))
            helper(r+1,c, curr+"D")
            helper(r-1,c, curr+"U")
            helper(r, c+1, curr+"R")
            helper(r, c-1, curr+"L")
            vis.remove((r,c))
            return
            
        helper(0,0,"")
        return ans
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends