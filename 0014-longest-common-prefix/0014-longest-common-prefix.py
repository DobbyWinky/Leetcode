class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen=float('inf')
        for s in strs:
            if len(s)<minLen:
                minLen=len(s)
        firstStr = strs[0]
        ans=""
        for k in range(minLen):
            for i in range(1, len(strs)):
                if firstStr[k]!=strs[i][k]:
                    return ans
            ans+=firstStr[k]
        return ans
        