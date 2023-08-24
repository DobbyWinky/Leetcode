class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        n=len(s)
        hash=collections.defaultdict(int)
        ans=0
        while right<n:
            hash[s[right]]+=1
            if hash[s[right]]>1:
                while left<right and s[left]!=s[right]:
                    hash[s[left]]-=1
                    left+=1
                hash[s[left]]-=1
                left+=1
            ans=max(ans, right-left+1)
            right+=1
        return ans
            
        