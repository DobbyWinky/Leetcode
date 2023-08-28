class Solution:
    def calculate(self, s: str) -> int:
        i=0
        curr=0
        curr_sign='+'
        ans=0
        while i<len(s):
            if s[i].isdigit():
                while i<len(s) and s[i].isdigit():
                    curr=curr*10+int(s[i])
                    i+=1
                i-=1
                if curr_sign=='+':
                    ans+=curr
                    prev=curr
                elif curr_sign=='-':
                    ans-=curr
                    prev=-curr
                elif curr_sign=='*':
                    ans-=prev
                    ans+=prev*curr
                    prev=prev*curr
                    
                else:
                    ans-=prev
                    ans+=int(prev/curr)
                    prev=int(prev/curr)
                curr=0
            elif s[i]!=' ':
                curr_sign=s[i]
            i+=1
        return ans
                    
            
        