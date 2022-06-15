type CustomStack struct {
    stack []int
    maxSize int
}


func Constructor(maxSize int) CustomStack {
    return CustomStack{make([]int, 0), maxSize}
}


func (this *CustomStack) Push(x int)  {
    if len(this.stack)<this.maxSize {
        this.stack=append(this.stack, x)
    }
}


func (this *CustomStack) Pop() int {
    if len(this.stack)==0 {
        return -1
    }
    x:=this.stack[len(this.stack)-1]
    this.stack=this.stack[:len(this.stack)-1]
    return x
}


func (this *CustomStack) Increment(k int, val int)  {
    if k>len(this.stack) {
        k=len(this.stack)
    }
    for i:=0;i<k;i++ {
        this.stack[i]+=val
    }
}


/**
 * Your CustomStack object will be instantiated and called as such:
 * obj := Constructor(maxSize);
 * obj.Push(x);
 * param_2 := obj.Pop();
 * obj.Increment(k,val);
 */