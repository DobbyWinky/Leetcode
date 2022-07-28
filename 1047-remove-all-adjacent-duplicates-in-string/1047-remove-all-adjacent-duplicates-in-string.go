func removeDuplicates(s string) string {
    stack:=make([]byte, 0)
    for i:=0;i<len(s);i++ {
        if len(stack)==0 {
            stack=append(stack, s[i])
        }else {
            if stack[len(stack)-1]==s[i] {
                stack=stack[:len(stack)-1]
            }else {
                stack=append(stack, s[i])
            }
        }
    }
    return string(stack)
}