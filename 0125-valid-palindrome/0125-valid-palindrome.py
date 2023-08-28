class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        n=len(s)
        r=n-1
        s=s.lower()
        while l<=r:
            if not (s[l].isalpha() or s[l].isdigit()):
                l+=1
            elif not (s[r].isalpha() or s[r].isdigit()):
                r-=1
            elif s[l]!=s[r]:
                return False
            else:
                l+=1
                r-=1
        return True
        