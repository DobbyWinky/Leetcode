/*
Time - O(n)
Space - O(n)
*/
func isValid(s string) bool {
    if len(s)==0 {
        return true
    }
    stack:=make([]byte, 0)
    for i:=0;i<len(s);i++ {
        if len(stack)==0 || s[i]=='(' || s[i]=='[' || s[i]=='{'{
            stack=append(stack, s[i])
            continue
        }
        if s[i]==')' && stack[len(stack)-1]!='(' {
            return false
        }else if s[i]=='}' && stack[len(stack)-1]!='{' {
            return false
        }else if s[i]==']' && stack[len(stack)-1]!='[' {
            return false
        }else {
            stack=stack[:len(stack)-1]
        }
    }
    return len(stack)==0
}