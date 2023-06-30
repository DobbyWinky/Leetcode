#User function Template for python3

class Solution:
    
    #Function to find maximum of minimums of every window size.
    def maxOfMin(self,arr,n):
        left=[-1]*n
        right=[n]*n
        stack=[]
        for i in range(n):
            while len(stack)!=0 and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if len(stack)!=0:
                left[i]=stack[-1]
            stack.append(i)
        stack.clear()
        for i in range(n-1,-1,-1):
            while len(stack)!=0 and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if len(stack)!=0:
                right[i]=stack[-1]
            stack.append(i)
        ans=[-1]*(n+1)
        for i in range(n):
            x=right[i]-left[i]-1
            ans[x]=max(ans[x],arr[i])
        for i in range(n-1, 0, -1):
            ans[i]=max(ans[i],ans[i+1])
        return ans[1:]
            
    # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.maxOfMin(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()

# } Driver Code Ends