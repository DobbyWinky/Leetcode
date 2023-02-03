#Your task is to complete this function
#Your should return the required output
import collections
class Solution:
    def maxLen(self, n, arr):
        hash=collections.defaultdict(int)
        sum=0
        maxl=0
        for i,a in enumerate(arr):
            sum+=a
            if sum==0:
                maxl=i+1
                continue
            if sum in hash:
                maxl=max(maxl,i-hash[sum])
            else:
                hash[sum]=i
        return maxl
            
        #Code here


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends