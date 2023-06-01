class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for c in s:
            if len(stack)==0:
                stack.append(c)
                continue
            if c==')'and stack[-1]=='(':
                stack.pop()
            elif c=='}' and stack[-1]=='{':
                stack.pop()
            elif c==']' and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(c)
        if len(stack)==0:
            return True
        return False
        