#User function Template for python3

class Solution:
    def help_classmate(self, arr, n):
        stack=[]
        ans=[-1]*n
        for i, a in enumerate(arr):
            if len(stack)==0:
                stack.append([a,i])
                continue
            while len(stack)!=0 and stack[-1][0]>a:
                pop=stack.pop()
                ans[pop[1]]=a
            stack.append([a, i])
        return ans
                
        # Your code goes here
        # Return the list


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [ int(x) for x in input().split() ]
        obj = Solution()
        result = obj.help_classmate(arr,n)
        for i in result:
            print(i,end=' ')
        print()

# } Driver Code Ends