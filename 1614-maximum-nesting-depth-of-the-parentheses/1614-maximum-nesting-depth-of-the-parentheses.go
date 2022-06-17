func maxDepth(s string) int {
    max:=0
    ans:=0
    stack:=make([]byte, 0)
    for i:=0;i<len(s);i++ {
        if s[i]=='(' {
            stack=append(stack, s[i])
            ans++    
        }
        if s[i]==')' {
            stack=stack[:len(stack)-1]
            ans--
        }
        if ans>max {
            max=ans
        }
    }
    return max
}