type MovingAverage struct {
    queue []int
    size int
}


func Constructor(size int) MovingAverage {
    return MovingAverage{make([]int, 0), size}
}


func (this *MovingAverage) Next(val int) float64 {
    if len(this.queue)==this.size {
        this.queue=this.queue[1:]
    }
    this.queue=append(this.queue, val)
    avg:=0.0
    for i:=0;i<len(this.queue);i++ {
        avg+=float64(this.queue[i])
    }
    return avg/float64(len(this.queue))
}


/**
 * Your MovingAverage object will be instantiated and called as such:
 * obj := Constructor(size);
 * param_1 := obj.Next(val);
 */