func plusOne(digits []int) []int {
    if digits[len(digits)-1]==9 {
        carry:=1
        for i:=len(digits)-1;i>=0;i-- {
            sum:=(digits[i]+carry)%10
            carry=(digits[i]+carry)/10
            digits[i]=sum
        }
        if carry!=0 {
            digits=append([]int{carry}, digits...)
        }
        return digits
    }else {
        digits[len(digits)-1]++
        return digits
    }
}