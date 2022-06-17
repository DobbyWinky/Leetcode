type OrderedStream struct {
    stream []string
    ptr int
}


func Constructor(n int) OrderedStream {
    return OrderedStream{make([]string, n), 0}
}


func (this *OrderedStream) Insert(idKey int, value string) []string {
    this.stream[idKey-1]=value
    if this.stream[this.ptr]=="" {
        return nil
    }
    ans:=make([]string, 0)
    for this.ptr<len(this.stream)&&this.stream[this.ptr]!="" {
        ans=append(ans, this.stream[this.ptr])
        this.ptr++
    }
    return ans
}


/**
 * Your OrderedStream object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Insert(idKey,value);
 */