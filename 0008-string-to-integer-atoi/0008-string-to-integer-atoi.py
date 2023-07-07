class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        new_s=s.lstrip("0")
        n=len(new_s)
        if n==0:
            return 0
        if len(new_s)!=len(s) and (new_s[0]=='+' or new_s[0]=='-'):
            return 0
        s=new_s
        sign=0
        digitFound=False
        signFound=False
        if s[0]=='-':
            sign=1
        prev=0
        ans=0
        for i in range(n):
            if not s[i].isdigit():
                if not digitFound and s[i]!='+' and s[i]!='-':
                    return 0
                elif s[i]!='+' and s[i]!='-':
                    break
                elif signFound and not digitFound:
                    return 0
                elif signFound and digitFound:
                    break
                if s[i]=='+' or s[i]=='-':
                    signFound=True
            else:
                digitFound=True
                ans=prev*10+int(s[i])
                prev=ans
        if sign:
            ans=ans*-1
        if ans>2147483647:
            return 2147483647
        elif ans<-2147483648:
            return -2147483648
        return ans
                
            
        
        