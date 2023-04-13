class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split(" ")
        ans=""
        j=len(words)-1
        while j>=0:
            if words[j]!='':
                ans+=words[j]+" "
            j-=1
        return ans[:-1]
                    
            
        