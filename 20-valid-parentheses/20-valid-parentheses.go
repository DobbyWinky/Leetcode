/*
Time - O(n)
Space - O(n)
*/
func isValid(s string) bool {
    stack:=make([]byte,0) 
    for i:=0;i<len(s);i++ {
        if len(stack)==0 || s[i]=='(' || s[i]=='[' || s[i]=='{'{
            stack=append(stack, s[i])
        }
        if s[i]==')' {
            if stack[len(stack)-1]!='(' {
                return false
            }
            stack=stack[:len(stack)-1]
        }
        if s[i]=='}' {
            if stack[len(stack)-1]!='{' {
                return false
            }
            stack=stack[:len(stack)-1]
        }
        if s[i]==']' {
            if stack[len(stack)-1]!='[' {
                return false
            }
            stack=stack[:len(stack)-1]
        }
    }
    if len(stack)==0 {
        return true
    }
    return false
}