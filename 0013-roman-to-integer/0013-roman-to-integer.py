class Solution:
    def romanToInt(self, s: str) -> int:
        ans=0
        n=len(s)
        romanTable={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        for i in range(n-1):
            if romanTable[s[i+1]]<=romanTable[s[i]]:
                ans+=romanTable[s[i]]
            else:
                ans-=romanTable[s[i]]
        ans+=romanTable[s[n-1]]
        return ans