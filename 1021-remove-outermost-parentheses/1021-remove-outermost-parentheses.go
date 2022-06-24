func removeOuterParentheses(s string) string {
    var ans []rune
    stack:=make([]rune, 0)
    for _, w:= range s {
        if len(stack)==0 {
            stack=append(stack, w)
        }else if len(stack)==1 && w==')' {
            stack=stack[:len(stack)-1]
        }else {
            ans=append(ans, w)
            if w==')' {
                stack=stack[:len(stack)-1]
            }else {
                stack=append(stack, w)
            }
        }
    }
    return string(ans)
}