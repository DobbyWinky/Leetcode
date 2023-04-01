class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        count=[0]*26
        for w in word1:
            count[ord(w)-97]+=1
        for w in word2:
            count[ord(w)-97]-=1
        for i in range(26):
            if abs(count[i])>3:
                return False
        return True
            
                
            
        