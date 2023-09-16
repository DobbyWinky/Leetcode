class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        n=len(s)
        i=0
        while i<n:
            if s[i]!=']':
                stack.append(s[i])
                i+=1
            else:
                repeat=""
                while stack[-1]!='[':
                    repeat=stack.pop()+repeat
                stack.pop()
                k=""
                while stack and stack[-1].isdigit():
                    k=stack.pop()+k
                stack.append(int(k)*repeat)
                i+=1
        return "".join(stack)
                
        
        