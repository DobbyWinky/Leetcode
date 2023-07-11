class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        if len(haystack)<len(needle):
            return -1
        i=0
        match=True
        while i<len(haystack):
            if haystack[i]==needle[0]:
                for j in range(1, len(needle)):
                    if i+j>=len(haystack):
                        return -1
                    if needle[j]!=haystack[i+j]:
                        match=False
                        break
                if match:
                    return i
            match=True
            i+=1
        return -1
        