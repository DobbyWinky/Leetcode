type MinStack struct {
    stack []int
    minStack [][2]int
}


func Constructor() MinStack {
    return MinStack{make([]int, 0), make([][2]int, 0)}
}


func (this *MinStack) Push(val int)  {
    if len(this.stack)==0 {
        this.stack=append(this.stack, val)
        this.minStack=append(this.minStack, [2]int{val, 1})
        return
    }
    this.stack=append(this.stack, val)
    if val<this.minStack[len(this.minStack)-1][0] {
        this.minStack=append(this.minStack, [2]int{val, 1})
    }else if val==this.minStack[len(this.minStack)-1][0] {
        this.minStack[len(this.minStack)-1][1]++
    }
}


func (this *MinStack) Pop()  {
    if this.minStack[len(this.minStack)-1][0]==this.stack[len(this.stack)-1] {
        this.minStack[len(this.minStack)-1][1]--
        if this.minStack[len(this.minStack)-1][1]==0 {
            this.minStack=this.minStack[:len(this.minStack)-1]
        }
    }
    this.stack=this.stack[:len(this.stack)-1]
}


func (this *MinStack) Top() int {
    currStack:=this.stack
    return currStack[len(currStack)-1]
}


func (this *MinStack) GetMin() int {
    currMinStack:=this.minStack
    return currMinStack[len(currMinStack)-1][0]
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */