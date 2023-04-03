class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        ans=[]
        def helper(index, curr: List[str]):
            if index==n:
                print(curr)
                temp=curr[:]
                ans.append(temp)
                return
            for i in range(index, n):
                checkStr=s[index:i+1]
                if checkStr != checkStr[::-1]:
                    continue
                curr.append(s[index:i+1])
                helper(i+1, curr)
                curr.pop()
        helper(0,[])
        return ans
                
        