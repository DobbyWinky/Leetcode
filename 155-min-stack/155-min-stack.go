/*
Time - O(1)
Space - O(2n)
*/
type MinStack struct {
    stack [][2]int
}


func Constructor() MinStack {
    return MinStack{make([][2]int, 0)}
}


func (this *MinStack) Push(val int)  {
    if len(this.stack)==0 {
        this.stack=append(this.stack, [2]int{val, val})
    }else {
        this.stack=append(this.stack, [2]int{val, min(this.stack[len(this.stack)-1][1], val)})
    }
}

func min(i,j int) int {
    if i<j {
        return i
    }
    return j
}

func (this *MinStack) Pop()  {
    this.stack=this.stack[:len(this.stack)-1]
}


func (this *MinStack) Top() int {
    return this.stack[len(this.stack)-1][0]
}


func (this *MinStack) GetMin() int {
    return this.stack[len(this.stack)-1][1]
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */