class Solution:
    def calculate(self, s: str) -> int:
        curr=res=prev=0
        curr_sign='+'
        i=0
        n=len(s)
        while i<n:
            if s[i].isdigit():
                while i<n and s[i].isdigit():
                    curr=curr*10+int(s[i])
                    i+=1
                i-=1
                if curr_sign=='+':
                    res+=curr
                    prev=curr
                elif curr_sign=='-':
                    res-=curr
                    prev=-curr
                elif curr_sign=='*':
                    res-=prev
                    res+=prev*curr
                    prev=prev*curr
                elif curr_sign=='/':
                    res-=prev
                    res+=int(prev/curr)
                    prev=int(prev/curr)
                curr=0
            elif s[i]!=' ':
                curr_sign=s[i]
                
            i+=1
        return res
        