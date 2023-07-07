class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        n=len(s)
        if n==0:
            return 0
        i=0
        sign=0
        if s[0]=='-':
            sign=1
            i+=1
        if s[0]=='+':
            i+=1
        prev=0
        ans=0
        while i<n:
            if not s[i].isdigit():
                break
            else:
                ans=prev*10+int(s[i])
                prev=ans
            i+=1
        if sign:
            ans=ans*-1
        if ans>2147483647:
            return 2147483647
        elif ans<-2147483648:
            return -2147483648
        return ans
                
            
        
        