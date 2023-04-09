class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if goal[i:]+goal[:i]==s:
                return True
        return False