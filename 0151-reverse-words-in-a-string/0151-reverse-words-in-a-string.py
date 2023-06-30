class Solution:
    def reverseWords(self, s: str) -> str:
        # def reverse(s):
        #     n=len(s)
        #     i=0
        #     j=n-1
        #     while i<=j:
        #         s[i],s[j]=s[j],s[i]
        #         i+=1
        #         j-=1
        #     return s
        words = s.split(" ")
        for word in words:
            word.strip()
        i=len(words)-1
        ans=""
        while i>=0:
            if words[i]!="":
                ans+=words[i]+" "
            i-=1
        return ans[:len(ans)-1]
        