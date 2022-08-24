class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        window = 0
        wordSet = dict()
        while j<len(s):
            if s[j] in wordSet:
                i = max(i, wordSet[s[j]])
            wordSet[s[j]]=j+1
            window=max(window, j-i+1)
            j+=1
        return window