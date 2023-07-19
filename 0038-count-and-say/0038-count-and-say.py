class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        if n==2:
            return "11"
        s="11"
        for i in range(3,n+1):
            s+="&"
            count=1
            t=""
            for j in range(1,len(s)):
                if s[j]==s[j-1]:
                    count+=1
                else:
                    t+=str(count)
                    t+=s[j-1]
                    count=1
            s=t
            print(s)
        return s
                    
                    