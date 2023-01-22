class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def __init__(self):
        self.count=0
        
    def inversionCount(self, arr, n):
        temp=[0]*n
        self.mergeSort(arr,temp, 0, n-1)
        return self.count
    
    def mergeSort(self, arr, temp, lo, hi):
        if lo<hi:
            mid=(lo+hi)//2
            self.mergeSort(arr,temp, lo, mid)
            self.mergeSort(arr,temp, mid+1, hi)
            self.merge(arr, temp, lo,mid, hi)
    
    def merge(self, arr,temp, lo, mid, hi):
        i=lo
        j=mid+1
        k=lo
        while i<=mid and j<=hi:
            if arr[i]<=arr[j]:
                temp[k]=arr[i]
                k+=1
                i+=1
            else:
                self.count+=(mid-i+1)
                temp[k]=arr[j]
                k+=1
                j+=1
        while i<=mid:
            temp[k]=arr[i]
            k+=1
            i+=1
            
        while j<=hi:
            temp[k]=arr[j]
            k+=1
            j+=1
        
        for p in range(lo,hi+1):
            arr[p]=temp[p]
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends