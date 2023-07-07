class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        if n==0:
            return ""
        if n==1:
            return strs[0]
        pre=strs[0]
        for i in range(1,n):
            for j in range(len(strs[i])):
                if j<len(pre) and strs[i][j]!=pre[j]:
                    pre=strs[i][:j]
                    break
            pre=strs[i] if len(strs[i])<len(pre) else pre
        return pre
                    
                    
        
        