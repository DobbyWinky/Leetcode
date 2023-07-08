class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        def check(text,pattern):
            m=len(pattern)
            n=len(text)
            d=26
            q=1e9+7
            i=0
            j=0
            t=0
            p=0
            h=1
            for i in range(m-1):
                h=(h*d)%q
            for i in range(m):
                p=(p*d+ord(pattern[i]))%q
                t=(t*d+ord(text[i]))%q
            for i in range(n-m+1):
                if t==p:
                    j=0
                    while j<m:
                        if pattern[j]!=text[i+j]:
                            break
                        j+=1
                    if j==m:
                        return True
                if i<n-m:
                    t=(d*(t-ord(text[i])*h)+ord(text[i+m]))%q
                    if t<0:
                        t+=q   
            return False
            
        temp=a
        ans=1
        while len(a)<len(b):
            a+=temp
            ans+=1
        if check(a,b):
            return ans
        a+=temp
        if check(a,b):
            return ans+1
        return -1
            
        