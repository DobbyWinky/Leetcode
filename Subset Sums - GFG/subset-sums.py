#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
	    ans=[]
	    def helper(idx, curr):
	        if idx==N:
	            ans.append(curr)
	            return
	        helper(idx+1, curr)
	        helper(idx+1, curr+arr[idx])
	    helper(0,0)
	    return ans
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends