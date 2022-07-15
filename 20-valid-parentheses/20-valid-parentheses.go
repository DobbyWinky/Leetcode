func isValid(s string) bool {
    stack:=make([]byte, 0)
    for i:=0;i<len(s);i++ {
        if len(stack)==0 {
            if s[i]==')' || s[i]=='}' || s[i]==']' {
                return false
            }
            stack=append(stack, s[i])
        }else if s[i]==')' {
            if stack[len(stack)-1] != '(' {
                return false
            }
            stack=stack[:len(stack)-1]
        }else if s[i]==']' {
            if stack[len(stack)-1] != '[' {
                return false
            }
            stack=stack[:len(stack)-1]
        }else if s[i]=='}' {
            if stack[len(stack)-1] != '{' {
                return false
            }
            stack=stack[:len(stack)-1]
        }else {
            stack=append(stack, s[i])
        }
    }
    if len(stack)!=0 {
        return false
    }
    return true
}