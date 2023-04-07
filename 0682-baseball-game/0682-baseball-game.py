class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        sum=0
        for op in operations:
            if len(stack)==0:
                stack.append(int(op))
                continue
            if op=='C':
                stack.pop()
            elif op=='D':
                top=stack[-1]
                stack.append(top*2)
            elif op=='+':
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(op))
        for s in stack:
            sum+=s
        return sum
                
        